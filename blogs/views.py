from django.shortcuts import render,HttpResponse,redirect 
from .models import blogpost,blogComment
from django.contrib import messages
from blogs.templatetags import extras
from django.core.paginator import Paginator,EmptyPage

# Create your views here.
def bloglist(request):
    bloglist=blogpost.objects.all()
    p=Paginator(bloglist[::-1],7)

    page_num=request.GET.get('page',1)
    tpage=p.num_pages
    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)
    return render(request,'blogs/bloglist.html',{'blists':page,'tpage':tpage})
 

def blogPost(request,name):
    post=blogpost.objects.filter(blog_title=name)
    comments=blogComment.objects.filter(linked_post=post[0].id,parent=None)
    replies=blogComment.objects.filter(linked_post=post[0].id).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sn not in replyDict.keys():
            replyDict[reply.parent.sn]=[reply]
        else:
            replyDict[reply.parent.sn].append(reply)
    commentl=blogComment.objects.all()
    bloglist=blogpost.objects.all()
    # replies=blogComment.objects.filter(parent=)
    print(comments)
    context={
        'posts':post[0],
        'blists':bloglist[:10:-1],
        'comments':comments[::-1],
        'commentl':commentl[:5:-1],
        'replyDict':replyDict}
    return render(request,'blogs/blogpost.html',context)


def blogcomment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        username=request.POST.get("username")
        user_email=request.POST.get("email")
        blog_title=request.POST.get("blog_title")
        post=blogpost.objects.get(blog_title=blog_title)
        parentsn=request.POST.get("parentsn")
        if parentsn=="":
            comment=blogComment(comment=comment,username=username,usermail=user_email,linked_post=post)
            comment.save()

        else:
            parent=blogComment.objects.get(sn=parentsn)
            comment=blogComment(comment=comment,username=username,usermail=user_email,linked_post=post,parent=parent)
            comment.save()
      
       

    return redirect(f"/blogs/blogpost/{blog_title}")