from django.db import models

# Create your models here.
 
class blogpost(models.Model):

    blog_title=models.CharField(max_length=50,default="")
    blog_content=models.CharField(max_length=5000,default="")
    blog_writer=models.CharField(max_length=50,default="scienceforum")
    blod_date=models.DateField
    thumbnail=models.ImageField(upload_to="img/blogimg",default="/static/img/logo.png")

    def __str__(self):
        return self.blog_title
