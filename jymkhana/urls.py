from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),         
    url(r'^parliament/', include('parliament.urls')),
    url(r'', include('home.urls')),
	url(r'^Fmc/', include('fmc.urls')),
	url(r'^Gnsc/', include('gnsc.urls')),
	url(r'^Cultural/', include('cultural.urls')),
	url(r'^Sntc/', include('sntc.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)