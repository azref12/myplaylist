from rest_framework import serializers
from . models import *

class PlaylistSerializer (serializers.ModelSerializer) :
    
    class Meta :
        model = playlist
        fields = ['id_playlist','id_category','id_genre','title','images_list',
                  'director','writer','network','episodes','release_date','runtime','language','country']
        # fields = "__all__"