from django.conf.urls import url
from rest_framework import routers
from playlist import views
from .views import *

router = routers.DefaultRouter()

urlpatterns = [

    url(r'list/$', views.PlayList_List.as_view(), name='PlayList_List'),
    url(r'list_detail/(?P<pk>[0-9]+)$', views.PlayList_Detail.as_view(), name='PlayList_Detail'),
    url(r'getbytitle/$', views.getbytitle),
    # url(r'searchbytitle/$', views.search_by_title),
    
]

urlpatterns += router.urls