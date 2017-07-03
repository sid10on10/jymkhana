from django.conf.urls import url
from . import views



urlpatterns = [
	
	url(r'^$', views.sntc, name='sntc'),
    	url(r'^clubs/aero_modelling$', views.aero_modelling, name='aero_modelling'),
	url(r'^clubs/astronomy$', views.astronomy, name='astronomy'),
	url(r'^clubs/cef$', views.clubofeconomicsandfinance, name='cef'),
	url(r'^clubs/robotics$', views.robotics, name='robotics'),
	url(r'^clubs/sae_collegiate$', views.sae_collegiate, name='sae_collegiate'),
	url(r'^clubs/cops$', views.cops, name='cops'),
	url(r'^clubs/green$', views.green, name='green'),
	url(r'^clubs/troc$', views.troc, name='troc'),
	url(r'^teams/auv$', views.auv, name='auv'),
	url(r'^teams/vocowsa$', views.vocowsa, name='vocowsa'),
	url(r'^teams/baja$', views.baja, name='baja'),
]
