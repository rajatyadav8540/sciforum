from django.shortcuts import render,HttpResponse
from .models import blogpost

# Create your views here.
def bloglist(request):
    bloglist=blogpost.objects.all()
    return render(request,'blogs/bloglist.html',{'blists':bloglist[::-1]})
 

def blogPost(request,name):
    post=blogpost.objects.filter(blog_title=name)
<<<<<<< HEAD
    return render(request,'blogs/blogpost.html',{'posts':post[0]})

=======
    bloglist=blogpost.objects.all()
    return render(request,'blogs/blogpost.html',{'posts':post[0],'blists':bloglist[:10:-1]})
>>>>>>> ccf7c85a8b62860c9add5123abfc1d0722286b58
