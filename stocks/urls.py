from django.urls import path
from stocks import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('stocks/(?P<pk>.*)$', views.index, name='stock-detail'),
    path('(?P<string>[\w\-]+)/$', views.detail, name='stock-detail'),
    path('detail/<slug:primary_key>', views.detail, name='stock-detail'),

]