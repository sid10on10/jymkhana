from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^$', 'sntc.views.home', name='home'),
    url(r'^clubs/aero_modelling$', 'sntc.views.amc', name='amc'),
    url(r'^clubs/astronomy$', 'sntc.views.astro', name='astro'),
    url(r'^clubs/cops$', 'sntc.views.cops', name='cops'),
    url(r'^clubs/green$', 'sntc.views.green', name='green'),
    url(r'^clubs/troc$', 'sntc.views.troc', name='troc'),
    url(r'^clubs/robotics$', 'sntc.views.robotics', name='robotics'),
    url(r'^clubs/sae$', 'sntc.views.sae', name='sae'),
    url(r'^clubs/cef$', 'sntc.views.cef', name='cef'),
    url(r'^teams/trident$', 'sntc.views.trident', name='trident'),
    url(r'^teams/vocowa$', 'sntc.views.vocowa', name='vocowa'),
    url(r'^teams/auv$', 'sntc.views.auv', name='auv'),
    url(r'^app/$', 'sntc.views.app', name='app'),
]