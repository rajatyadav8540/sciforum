from django.db import models

# Create your models here.

class event(models.Model):

    event_name= models.CharField(max_length=50)
    event_content= models.CharField(max_length=1000)