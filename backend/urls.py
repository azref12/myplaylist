from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^category/', include('category.urls')),
    url(r'^kdrama/', include('kdrama.urls')),
    url(r'^playlist/', include('playlist.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)