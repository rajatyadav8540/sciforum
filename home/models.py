from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class TeamProfile(models.Model):

    Profile_title=models.CharField(max_length=50,default="")
    Profile_Post=models.CharField(max_length=50,default="member")
    Profile_content=models.CharField(max_length=5000,default="")
    Profile_email=models.CharField(max_length=50,default="scienceforum")
    Profile_thumbnail=models.ImageField(upload_to="img/profiles",default="img/blogimg/science-1182713_1920.jpg")

    def __str__(self):
        return self.Profile_title

class ScientistGallery(models.Model):

    Scientist_title=models.CharField(max_length=50,default="")
    Scientist_content=RichTextField(max_length=5000,default="")
    Scientist_thumbnail=models.ImageField(upload_to="img/Scientist",default="img/blogimg/science-1182713_1920.jpg")

    def __str__(self):
        return self.Scientist_title