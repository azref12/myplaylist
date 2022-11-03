from django.db import models
from playlist.models import playlist

class recommendation (models.Model) :
    id_recommendation = models.AutoField(primary_key=True)
    id_playlist = models.ForeignKey(playlist, related_name='idplaylist', on_delete=models.CASCADE)
