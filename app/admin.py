from django.contrib import admin
from .models import TrainImagesOfCancer, TrainImagesNotCancer, ConvnetModel, Usage
from .trainer import trainer

# Register your models here.

def TrainTheModel(modeladmin, request, queryset):
    trainer()
TrainTheModel.short_description = "Train the convnet model"

class Convnet(admin.ModelAdmin):
    actions = [TrainTheModel]

admin.site.register(TrainImagesOfCancer)
admin.site.register(TrainImagesNotCancer)
admin.site.register(ConvnetModel, Convnet)
admin.site.register(Usage)