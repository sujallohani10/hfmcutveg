from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('carrotandcelery', views.carrotAndCelery, name='carrotandcelery'),
    url('post/ajax/calculateCarrrotCelery', views.calculateCarrrotCelery, name='calculateCarrrotCelery'),
    url('post/ajax/validate_amount', views.validate_amount, name='validate_amount'),
]