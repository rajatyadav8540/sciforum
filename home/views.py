from django.shortcuts import render
from .models import TeamProfile,ScientistGallery

# Create your views here.
def index(request):
    return render(request,'home/index.html')
 
def about(request):
    profileDetails=TeamProfile.objects.all()
    context={
             'profiles':profileDetails
    }
    return render(request,'home/about.html',context)

def scienceGallery(request):
    ScientistDetails=ScientistGallery.objects.all()
    context={
             'Scientists':ScientistDetails
    }
    return render(request,'home/scienceGallery.html',context)

def ScientistProfile(request,name):
    ScientistDetails=ScientistGallery.objects.all()
    ScientistDet=ScientistGallery.objects.filter(Scientist_title=name)
    context={
             'ScientistProf':ScientistDet[0],
             'Scientists':ScientistDetails
    }
    return render(request,'home/ScientistProfile.html',context)