from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='calculator'),
    url('post/ajax/calculateGrocery', views.calculateGrocery, name='calculateGrocery'),
    url('post/ajax/validate_amount', views.validate_amount, name='validate_amount'),
]