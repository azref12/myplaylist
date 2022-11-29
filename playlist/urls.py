from django.conf.urls import url
from rest_framework import routers
from playlist import views
from .views import *

router = routers.DefaultRouter()

urlpatterns = [

    url(r'list/$', views.playlist_list, name='playlist_list'),
    
]

urlpatterns += router.urls