from django.shortcuts import render
from stocks.models import Ticker
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from  django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView


def index(request):
    """View function for home page of site."""

    if request.method == 'GET':  # If the form is submitted
        search_query = request.GET.get('search_box', None)
        if search_query:
            try:
                ticker = get_object_or_404(Ticker, pk=search_query)
            except Exception as ex:
                return HttpResponseNotFound('<h3>Invalid Ticker Symbol </h3>')
            return render(request, 'stock_detail.html', context={'ticker': ticker})

    ticker_list = Ticker.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(ticker_list, 10)
    try:
        tickers = paginator.page(page)
    except PageNotAnInteger:
        tickers = paginator.page(1)
    except EmptyPage:
        tickers = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'tickers': tickers})



def detail(request, primary_key):
    """View function for the ticker detail page."""
    try:
        ticker = get_object_or_404(Ticker, pk=primary_key)
    except Exception as ex:
        return HttpResponseNotFound('<h3>Invalid Ticker Symbol </h3>')
    return render(request, 'stock_detail.html', context={'ticker' : ticker})
