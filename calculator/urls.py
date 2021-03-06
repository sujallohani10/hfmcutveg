from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('carrotandcelery', views.carrotAndCelery, name='carrotandcelery'),
    path('carrotbattons', views.carrotBattons, name='carrotbattons'),
    path('carrotcurls', views.carrotCurls, name='carrotcurls'),
    path('dicedpumpkin', views.dicedPumpkin, name='dicedpumpkin'),
    path('zucchini', views.zucchini, name='zucchini'),
    path('beetroot', views.beetroot, name='beetroot'),
    path('cauliflowerrice', views.cauliflowerRice, name='cauliflowerrice'),
    path('shreddedkale', views.shreddedKale, name='shreddedkale'),
    path('mixcapsicum', views.mixCapsicum, name='mixcapsicum'),
    path('stirfry', views.stirFry, name='stirfry'),
    path('coleslaw', views.coleslaw, name='coleslaw'),
    path('asianmix', views.asianMix, name='asianmix'),
    path('entertainmentpack', views.entertainmentPack, name='entertainmentpack'),
    url('post/ajax/calculateCommonMethod', views.calculateCommonMethod, name='calculateCommonMethod'),
    url('post/ajax/calculateMultipleItems', views.calculateMultipleItems, name='calculateMultipleItems'),
    url('post/ajax/validate_unit', views.validate_unit, name='validate_unit'),
]