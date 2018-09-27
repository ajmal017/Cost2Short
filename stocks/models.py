from django.db import models
from django.urls import reverse

# Create your models here.
class Ticker(models.Model):
    """Model representing a stock."""
    symbol = models.CharField(primary_key=True, max_length=5)
    curency = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    con = models.IntegerField()
    isin = models.CharField(max_length=255)
    rebate_rate = models.FloatField()
    fee_rate = models.FloatField()
    amount = models.CharField(max_length=255)

    def __str__(self):
        """US Ticker information """
        return self.title

    def get_absoulte_url(self):
        """return the url to access a detail record for the symbol."""
        return reverse('ticker-detail', args=[str(self.symbol)])