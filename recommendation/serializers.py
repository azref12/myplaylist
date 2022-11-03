from rest_framework import serializers
from . models import *
from playlist.serializers import PlaylistSerializer

class RecommendSerializer (serializers.ModelSerializer) :
    id_playlist = PlaylistSerializer (read_only=True)
    class Meta :
        model = recommendation
        fields = ['id_recommendation','id_playlist']
        # fields = "__all__"