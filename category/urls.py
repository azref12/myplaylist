from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'category/$', views.category_list),
    url(r'category_detail/(?P<pk>[0-9]+)$', views.category_detail),
    url(r'genre/$', views.genre_list),
    url(r'genre_detail/(?P<pk>[0-9]+)$', views.genre_detail),
]