from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class event(models.Model):
    
    event_name= models.CharField(max_length=50,default="")
    duration=models.CharField(max_length=50,default="",null=True)
    venue=models.CharField(max_length=50,default="",null=True)
    event_description=models.TextField(max_length=200,default="")
    event_content= RichTextField(max_length=2000,default="")

    def __str__(self):
        return self.event_name
  

class eventgallery(models.Model):

        event_image=models.ImageField(upload_to='img/eventimages',default="/static/img/logo.png")
        event_name=models.ForeignKey(event,on_delete=models.CASCADE)

        def __str__(self):
            return self.event_name