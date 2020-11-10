from django.shortcuts import render
from .models import event

# Create your views here.
def index(request):
    eventname=event.objects.all()
    context={
             'events':eventname
            
    }
    return render(request,'events/eventlist.html',context)
 