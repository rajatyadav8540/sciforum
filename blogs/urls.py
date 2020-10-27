from django.urls import path

from . import views

urlpatterns = [
    path('', views.bloglist, name='bloglist'),
    path('blogpost/<str:name>', views.blogPost, name='blogpost'),
     path('blogComment', views.blogcomment, name='blogComment'),

]