from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('carrotandcelery', views.carrotAndCelery, name='carrotandcelery'),
    path('carrotbattons', views.carrotBattons, name='carrotandcelery'),
    path('carrotcurls', views.carrotCurls, name='carrotcurls'),
    url('post/ajax/calculateCarrrotCelery', views.calculateCarrrotCelery, name='calculateCarrrotCelery'),
    url('post/ajax/calculateCarrotBattons', views.calculateCarrotBattons, name='calculateCarrotBattons'),
    url('post/ajax/calculateCarrotCurls', views.calculateCarrotBattons, name='calculateCarrotCurls'),
]