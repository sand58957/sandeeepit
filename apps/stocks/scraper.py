import requests
from bs4 import BeautifulSoup
import re
import decimal
from django.db import transaction
from .models import Stock, FundamentalSignal

def scrape_nepse_fundamentals():
    url = "https://nepsealpha.com/trading-signals/funda"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    session = requests.Session()
    session.headers.update(headers)

    # 1. Get the page to find the fsk key
    try:
        response = session.get(url, timeout=30)
        if response.status_code != 200:
            print(f"Failed to load page: {response.status_code}")
            return
    except Exception as e:
        print(f"Request error: {e}")
        return

    # Extract fsk from JS variable window.FORCE_URL_PARAM
    fsk_match = re.search(r'FORCE_URL_PARAM\s*=\s*([\'"]?)(.*?)\1;', response.text)
    if not fsk_match:
        print("Could not find fsk key")
        return
    
    fsk = fsk_match.group(2)
    print(f"Found fsk: {fsk}")

    # 2. Request the AJAX data
    ajax_url = f"https://nepsealpha.com/trading-signals/funda?fsk={fsk}&type=ajax"
    try:
        ajax_response = session.get(ajax_url, timeout=30)
        if ajax_response.status_code != 200:
            print(f"Failed to fetch AJAX data: {ajax_response.status_code}")
            return
    except Exception as e:
        print(f"AJAX request error: {e}")
        return

    # The response is an HTML fragment (tbody content)
    soup = BeautifulSoup(ajax_response.text, 'html.parser')
    rows = soup.find_all('tr')

    stocks_created = 0
    signals_updated = 0

    with transaction.atomic():
        for row in rows:
            cols = row.find_all('td')
            if not cols or len(cols) < 10:
                continue
            
            try:
                # Column indices based on Nepse Alpha structure:
                # 0: Symbol
                # 1: Ratios Summary
                # 2: Financial Strength
                # 3: Sector
                # 4: Daily Gain
                # 5: LTP
                # 6: PE
                # 7: PB
                # 8: PEG
                # 9: ROE
                # 10: ROA
                # 11: Graham
                # 12: Dividend Yield
                
                symbol_tag = cols[0].find('a')
                if not symbol_tag:
                    continue
                symbol = symbol_tag.get_text(strip=True)
                
                ratios_summary = cols[1].get_text(strip=True)
                financial_strength = cols[2].get_text(strip=True)
                sector = cols[3].get_text(strip=True)
                
                gain_text = cols[4].get_text(strip=True).replace('%', '').replace(',', '')
                ltp_text = cols[5].get_text(strip=True).replace(',', '')
                pe_text = cols[6].get_text(strip=True).replace(',', '')
                pb_text = cols[7].get_text(strip=True).replace(',', '')
                roe_text = cols[9].get_text(strip=True).replace('%', '').replace(',', '')
                yield_text = cols[12].get_text(strip=True).replace('%', '').replace(',', '')

                def to_decimal(val):
                    try:
                        # Clean the value: remove any non-numeric except dot and minus
                        clean_val = "".join(c for c in val if c.isdigit() or c in '.-')
                        return decimal.Decimal(clean_val) if clean_val else None
                    except:
                        return None

                # Update or create Stock
                stock, created = Stock.objects.get_or_create(
                    symbol=symbol,
                    defaults={'sector': sector}
                )
                if created:
                    stocks_created += 1
                else:
                    stock.sector = sector
                    stock.save()
                
                # Update or create FundamentalSignal
                FundamentalSignal.objects.update_or_create(
                    stock=stock,
                    defaults={
                        'ltp': to_decimal(ltp_text),
                        'daily_gain': to_decimal(gain_text),
                        'pe_ratio': to_decimal(pe_text),
                        'pb_ratio': to_decimal(pb_text),
                        'roe': to_decimal(roe_text),
                        'dividend_yield': to_decimal(yield_text),
                        'signal_summary': ratios_summary,
                        'financial_strength': financial_strength
                    }
                )
                signals_updated += 1

            except Exception as e:
                # print(f"Error parsing row: {e}")
                continue

    return f"Scraping complete. Created {stocks_created} new stocks, updated {signals_updated} signals."
