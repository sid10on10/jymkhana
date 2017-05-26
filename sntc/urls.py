from django.conf.urls import url
from . import views



urlpatterns = [
	
	url(r'^$', views.sntc, name='sntc'),
    url(r'^clubs/aero_modelling$', views.aero_modelling, name='aero_modelling'),
	url(r'^clubs/astronomy$', views.astronomy, name='astronomy'),
	url(r'^clubs/robotics$', views.robotics, name='robotics'),
	url(r'^clubs/sae_collegiate$', views.sae_collegiate, name='sae_collegiate'),
	url(r'^clubs/cops$', views.cops, name='cops'),
	url(r'^clubs/green$', views.green, name='green'),
	url(r'^clubs/clubofeconomicsandfinance$', views.clubofeconomicsandfinance, name='clubofeconomicsandfinance'),
]