from django.shortcuts import render
from .models import TeamProfile,ScientistGallery,admodal,testlink

# Create your views here.
def index(request):
    ads=admodal.objects.all()
    test=testlink.objects.all()
    return render(request,'home/index.html',{'ads':ads,'tests':test})
 
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