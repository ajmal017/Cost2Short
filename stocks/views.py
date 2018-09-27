from django.shortcuts import render
from stocks.models import Ticker
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from  django.core.exceptions import ObjectDoesNotExist

def index(request):
    """View function for home page of site."""

    ticker = Ticker.objects.first() # get the first object from query set as default

    return render(request, 'stock_detail.html', context={'ticker' : ticker})



def detail(request, primary_key):
    """View function for the ticker detail page."""
    try:
        ticker = get_object_or_404(Ticker, pk=primary_key)
    except Exception as ex:
        return HttpResponseNotFound('<h3>Invalid Ticker Symbol </h3>' + str(ex))
    return render(request, 'stock_detail.html', context={'ticker' : ticker})

