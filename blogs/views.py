from django.shortcuts import render,HttpResponse,redirect 
from .models import blogpost,blogComment
from django.contrib import messages

# Create your views here.
def bloglist(request):
    bloglist=blogpost.objects.all()
    return render(request,'blogs/bloglist.html',{'blists':bloglist[::-1]})
 

def blogPost(request,name):
    post=blogpost.objects.filter(blog_title=name)
    comments=blogComment.objects.filter(linked_post=post[0].id)
    commentl=blogComment.objects.all()
    bloglist=blogpost.objects.all()
    print(comments)
    context={
        'posts':post[0],
        'blists':bloglist[:10:-1],
        'comments':comments[::-1],
        'commentl':commentl[:5:-1]}
    return render(request,'blogs/blogpost.html',context)


def blogcomment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        username=request.POST.get("username")
        user_email=request.POST.get("email")
        blog_title=request.POST.get("blog_title")
        post=blogpost.objects.get(blog_title=blog_title)
        comment=blogComment(comment=comment,username=username,usermail=user_email,linked_post=post)
        comment.save()
      
       

    return redirect(f"/blogs/blogpost/{blog_title}")