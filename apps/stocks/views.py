from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock, FundamentalSignal
from .scraper import scrape_nepse_fundamentals
from django.contrib.auth.decorators import login_required
from core.decorators import admin_role_required

def stock_signals_list(request):
    signals = FundamentalSignal.objects.select_related('stock').all().order_by('stock__symbol')
    context = {
        'title': 'Fundamental Trading Signals',
        'signals': signals,
    }
    return render(request, 'stocks/signals_list.html', context)

@login_required(login_url='logIn')
@admin_role_required
def trigger_scraper(request):
    try:
        result = scrape_nepse_fundamentals()
        messages.success(request, result)
    except Exception as e:
        messages.error(request, f"Scraping failed: {e}")
    
    return redirect('stock_signals_list')
