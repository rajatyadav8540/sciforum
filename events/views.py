from django.shortcuts import render
from .models import event,eventgallery

# Create your views here.
def index(request):
    eventname=event.objects.all()
    eventimages=eventgallery.objects.all()
    context={
             'events':eventname,
             'gals':eventimages
    }
    return render(request,'events/eventlist.html',context)
 