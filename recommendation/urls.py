from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'recommendation/$', views.recommend_list),
    url(r'getbyid/(?P<pk>[0-9]+)$', views.playlist_id),
    
]