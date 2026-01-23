from django.urls import path
from .views import *

urlpatterns = [
    path('stocks/signals/', stock_signals_list, name='stock_signals_list'),
    path('stocks/scrape/', trigger_scraper, name='trigger_scraper'),
]
