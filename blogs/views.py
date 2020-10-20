from django.shortcuts import render,HttpResponse

# Create your views here.
def bloglist(request):
    return render(request,'blogs/bloglist.html')
