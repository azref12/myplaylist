from django.db import models
from django.core.files.storage import FileSystemStorage
from backend import settings
from category.models import category, genre
from kdrama.models import kdrama

fs = FileSystemStorage(base_url=settings.MEDIA_URL)

class playlist (models.Model) :
    id_playlist = models.AutoField(primary_key=True)
    id_category = models.ForeignKey(category, related_name='idcategory', on_delete=models.CASCADE)
    id_genre = models.ForeignKey(genre, related_name='idgenre', on_delete=models.CASCADE)
    id_kdrama = models.ForeignKey(kdrama, related_name='idkdrama', on_delete=models.CASCADE)