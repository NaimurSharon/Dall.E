from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    prompt = models.CharField(max_length=100, blank=False, null=False)
    photo = models.CharField(max_length=500, blank=False, null=False)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)

class Photo(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    photo = models.CharField(max_length=500, blank=False, null=False)
    prompt = models.CharField(max_length=100, blank=True, null=True)

    