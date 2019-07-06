from django.contrib import admin
from .models import TrainImagesOfCancer, TrainImagesNotCancer
# Register your models here.

admin.site.register(TrainImagesOfCancer)
admin.site.register(TrainImagesNotCancer)