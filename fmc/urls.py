from django.conf.urls import url
from . import views



urlpatterns = [
	
	url(r'^$', views.fmc, name='fmc'),
    url(r'^Clubs/Animation$', views.animation, name='animation'),
	url(r'^Clubs/Cine$', views.cine, name='cine'),
	url(r'^Clubs/Design$', views.design, name='design'),
	url(r'^Clubs/Media$', views.media, name='media'),
	url(r'^Clubs/Outreach$', views.outreach, name='outreach'),
	url(r'^Clubs/Photography$', views.photography, name='photography'),
]