from django.conf.urls import url
from . import views



urlpatterns = [
	
	url(r'^$', views.cultural, name='cultural'),
    url(r'^Clubs/fac$', views.animation, name='fac'),
	url(r'^Clubs/imc$', views.cine, name='imc'),
	url(r'^Clubs/lit$', views.design, name='lit'),
	url(r'^Clubs/masq$', views.media, name='masq'),
	url(r'^Clubs/quiz$', views.outreach, name='quiz'),
]