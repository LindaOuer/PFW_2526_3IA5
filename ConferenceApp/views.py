from django.shortcuts import render
from django.http import HttpResponse
from .models import Conference
from django.views.generic import ListView

# Create your views here.
def simple_view(request):
    return HttpResponse("This is a simple view.")

def home_view(request):
    return render(request, 'ConferenceApp/home.html')

def welcome(request, name):
    return render(
        request, 
        'ConferenceApp/welcome.html', 
        {'n': name}
    )

def listConferences(request):
    conferences = Conference.objects.all()
    return render(request, 'ConferenceApp/list.html', {'conferences': conferences})

class ConferenceListView(ListView):
    model = Conference
    template_name = 'ConferenceApp/list.html'
    context_object_name = 'conferences'