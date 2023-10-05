from django.db import models

# Create your models here.



class Image(models.Model):
    Name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts')
    