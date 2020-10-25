from django.shortcuts import render
from .models import TeamProfile

# Create your views here.
def index(request):
    return render(request,'home/index.html')
 
def about(request):
    profileDetails=TeamProfile.objects.all()
    context={
             'profiles':profileDetails
    }
    return render(request,'home/about.html',context)