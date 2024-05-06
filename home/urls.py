
from django.urls import path,include
from .views import *


urlpatterns = [

    path('', home, name='home'),
    path('aboutus', about, name='aboutus'),
    path('contactus', contact, name='contactus'),
    path('my_portfolio', portfolio, name='my_portfolio'),
    path('pricing', price, name='pricing'),
    path('my_services', services, name='my_services'),
]
