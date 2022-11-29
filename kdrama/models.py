from django.db import models
from django.core.files.storage import FileSystemStorage
from backend import settings
from category.models import category, genre

fs = FileSystemStorage(base_url=settings.MEDIA_URL)

class kdrama (models.Model) :
    id_kdrama = models.AutoField(primary_key=True)
    id_category = models.ForeignKey(category, related_name='id_category_id', on_delete=models.CASCADE)
    id_genre = models.ForeignKey(genre, related_name='id_genre_id', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    images_list = models.ImageField(upload_to='kdrama/', storage=fs, null=True, blank=True)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    episodes = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    runtime = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
