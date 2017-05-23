from django.conf.urls import url
from . import views



urlpatterns = [
	
	url(r'^$', views.cultural, name='cultural'),
    url(r'^Clubs/fac$', views.fac, name='fac'),
	url(r'^Clubs/imc$', views.imc, name='imc'),
	url(r'^Clubs/lit$', views.lit, name='lit'),
	url(r'^Clubs/masq$', views.masq, name='masq'),
	url(r'^Clubs/quiz$', views.quiz, name='quiz'),
]