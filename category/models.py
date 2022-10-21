from unittest.util import _MAX_LENGTH
from django.db import models

class category (models.Model) :
    id_category = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    
class genre (models.Model) : 
    id_genre = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=100)
    