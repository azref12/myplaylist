from django.conf.urls import url
from rest_framework import routers
from kdrama import views
from .views import *

router = routers.DefaultRouter()

urlpatterns = [

    url(r'kdrama_list/$', views.Kdrama_List.as_view(), name='Kdrama_List'),
    url(r'kdrama_detail/(?P<pk>[0-9]+)$', views.Kdrama_Detail.as_view(), name='Kdrama_Detail'),
    
]

urlpatterns += router.urls