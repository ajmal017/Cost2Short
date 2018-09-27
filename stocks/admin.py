from django.contrib import admin

# Register your models here.
from stocks.models import Ticker

admin.site.register(Ticker)