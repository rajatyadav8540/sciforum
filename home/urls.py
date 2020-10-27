from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('scienceGallery/',views.scienceGallery,name='ScienceGallery'),
    path('ScientistProfile/<str:name>', views.ScientistProfile, name='ScientistProfile'),

]