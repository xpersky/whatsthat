from django.db import models
from django.utils import timezone
# Create your models here.

class TrainImagesOfCancer(models.Model):
    image = models.ImageField(upload_to='images/cancer')

class TrainImagesNotCancer(models.Model):
    image = models.ImageField(upload_to='images/not_cancer')

class ConvnetModel(models.Model):
    name = models.CharField(max_length=20,default="What's that conv")

class Usage(models.Model):
    date = models.DateField(default=timezone.now())
    result = models.CharField(max_length=10,default="")