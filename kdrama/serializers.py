from rest_framework import serializers
from . models import *
from category.serializers import CategorySerializer, GenreSerializer

class KdramaSerializer (serializers.ModelSerializer) :
    # id_category = CategorySerializer (read_only=True)
    # id_genre = GenreSerializer (read_only=True)
    
    class Meta :
        model = kdrama
        fields = ['id_kdrama','id_category','id_genre','title','images_list',
                  'director','writer','network','episodes','release_date','runtime','language','country']
        # fields = "__all__"