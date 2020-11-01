from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class event(models.Model):
    
    event_name= models.CharField(max_length=50,default="")
    event_content= RichTextField(max_length=1000,default="")
    event_image=models.ImageField(upload_to='img/eventimages',default="/static/img/logo.png")

    def __str__(self):
        return self.event_name
