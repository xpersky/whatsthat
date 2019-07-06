from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.index,name='index'),
    path('about',views.index,name='index'),
    path('stats',views.index,name='index'),
    path('contact',views.index,name='index'),
    path('footer',views.index,name='index'),
    path('result',views.check,name='check')
]