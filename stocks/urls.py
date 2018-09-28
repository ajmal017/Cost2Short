from django.urls import path
from stocks import views
# from stocks.views import TickerList


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<slug:primary_key>', views.detail, name='stock-detail'),

]