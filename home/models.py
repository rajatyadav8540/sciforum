from django.db import models

# Create your models here.
class TeamProfile(models.Model):

    Profile_title=models.CharField(max_length=50,default="")
    Profile_Post=models.CharField(max_length=50,default="member")
    Profile_content=models.CharField(max_length=5000,default="")
    Profile_email=models.CharField(max_length=50,default="scienceforum")
    Profile_thumbnail=models.ImageField(upload_to="img/profiles",default="img/blogimg/science-1182713_1920.jpg")

    def __str__(self):
        return self.Profile_title