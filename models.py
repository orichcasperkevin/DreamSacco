from django.db import models

# Create your models here.
class Album(models.Model) :
    artist=models.CharField(max_length=250)
    album_tittle=models.CharField(max_length=200)
    genre =models.CharField(max_length=300)
class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=300)
    song_tittle= models.CharField(max_length=200)

