from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import ConferenceForm
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
from .serializers import ConferenceSerializer
# Create your views here.
class ConferenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conferences to be viewed or edited.
    - list() -> GET /conferences/
    - retrieve() -> GET /conferences/{id}/
    - create() -> POST /conferences/
    - update() -> PUT /conferences/{id}/
    - partial_update() -> PATCH /conferences/{id}/
    - destroy() -> DELETE /conferences/{id}/
    """
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    








class ConferenceCreateView(LoginRequiredMixin, CreateView):
    model = Conference
    fields = "__all__"
    template_name = 'ConferenceApp/conference_form.html'
class ConferenceDetailsView(DetailView):
    model = Conference
    template_name = 'ConferenceApp/conference_details.html'

def welcome(request):
    return HttpResponse("<h2>Welcome to the Conference App!</h2>")

def home(request, name):
    return render(request, 'ConferenceApp/home.html', {'name': name})

# Afficher la liste des conf. à partir de la DB
def listConferences(request):
    conferences = Conference.objects.all()
    return render(
        request, 
        'ConferenceApp/list_conferences.html',{'confs': conferences}
        )
    
class ConferenceListView(ListView):
    model = Conference
    template_name = 'ConferenceApp/list_conferences.html'
    context_object_name = 'conferences'
    

class ConferenceCreateView(CreateView):
    model = Conference
    # fields = "__all__" or []
    success_url = reverse_lazy("conference-listLV")
    form_class = ConferenceForm


class ConferenceUpdateView(UpdateView):
    model = Conference
    # fields = "__all__"
    success_url = reverse_lazy("conference-listLV")
    form_class = ConferenceForm


class ConferenceDeleteView(DeleteView):
    model = Conference
    context_object_name = "conference"
    success_url = reverse_lazy("conference-listLV")
