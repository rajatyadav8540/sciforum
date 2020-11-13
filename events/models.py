from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class event(models.Model):
    
    event_name= models.CharField(max_length=50,default="")
    duration=models.CharField(max_length=50,default="",null=True)
    venue=models.CharField(max_length=50,default="",null=True)
    event_description=models.TextField(max_length=800,default="")
    event_content= RichTextField(max_length=5000,default="")
    event_image1=models.ImageField(upload_to='img/eventimages',default="img/logo.png")
    event_image2=models.ImageField(upload_to='img/eventimages',default="img/logo.png")
    event_image3=models.ImageField(upload_to='img/eventimages',default="img/logo.png")

    def __str__(self):
        return self.event_name
  

