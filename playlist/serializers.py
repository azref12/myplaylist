from rest_framework import serializers
from . models import *
from category.serializers import CategorySerializer, GenreSerializer
from kdrama.serializers import KdramaSerializer

class PlaylistSerializer (serializers.ModelSerializer) :
    id_category = CategorySerializer (read_only=True)
    id_genre = GenreSerializer (read_only=True)
    id_kdrama = KdramaSerializer (read_only=True) 
    
    class Meta :
        model = playlist
        fields = ['id_playlist','id_category','id_genre','id_kdrama']
        # fields = "__all__"