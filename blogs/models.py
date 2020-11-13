from django.db import models
import datetime
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.
 
class blogpost(models.Model):

    blog_title=models.CharField(max_length=100,default="")
    blog_content=RichTextField(blank=True,null=True)
    blog_writer=models.CharField(max_length=50,default="scienceforum")
    blog_date=models.DateTimeField(default=now)
    thumbnail=models.ImageField(upload_to="img/blogimg",default="img/logo.png")

    def __str__(self):
        return self.blog_title +' by '+self.blog_writer


class blogComment(models.Model):

    sn=models.AutoField(primary_key=True)
    comment=models.TextField()
    linked_post=models.ForeignKey(blogpost,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=50,default="")
    usermail=models.CharField(max_length=50,default="",null=True)
    timestamp=models.DateTimeField(default=now)


    def __str__(self):
        return self.username 