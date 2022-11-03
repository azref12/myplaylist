from rest_framework import serializers
from . models import *
from category.serializers import CategorySerilaizer, GenreSerilaizer

class PlaylistSerializer (serializers.ModelSerializer) :
    id_category = CategorySerilaizer (read_only=True)
    id_genre = GenreSerilaizer (read_only=True)
    class Meta :
        model = playlist
        fields = ['id_playlist','id_category','id_genre','title','images_list',
                  'director','writer','network','episodes','release_date','runtime','language','country']
        # fields = "__all__"