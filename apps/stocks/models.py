from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.symbol

class FundamentalSignal(models.Model):
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE, related_name='fundamental')
    ltp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    daily_gain = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pe_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pb_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    roe = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dividend_yield = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    signal_summary = models.CharField(max_length=50, blank=True, null=True) # Strong, Weak, etc.
    financial_strength = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.stock.symbol} Signal"
