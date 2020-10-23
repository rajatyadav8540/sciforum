from django.db import models

# Create your models here.

class event(models.Model):
    
    event_name= models.CharField(max_length=50,default="")
    event_content= models.CharField(max_length=1000,default="")
    event_image=models.ImageField(upload_to='img/eventimages',default="/static/img/logo.png")

    def __str__(self):
        return self.event_name
