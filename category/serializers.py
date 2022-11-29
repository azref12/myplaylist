from rest_framework import serializers
from . models import *

class CategorySerializer (serializers.ModelSerializer) :
    
    class Meta :
        model = category
        fields = ['id_category', 'category_name']
        # fields = "__all__"
        
class GenreSerializer (serializers.ModelSerializer) :
    
    class Meta :
        model = genre
        fields = ['id_genre', 'genre']
        # fields = "__all__"