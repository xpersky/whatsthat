from django.db import models

# Create your models here.

class TrainImagesOfCancer(models.Model):
    image = models.ImageField(upload_to='images/cancer')

class TrainImagesNotCancer(models.Model):
    image = models.ImageField(upload_to='images/not_cancer')