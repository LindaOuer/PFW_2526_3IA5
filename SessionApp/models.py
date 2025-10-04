from django.db import models
from ConferenceApp.models import Conference

# Create your models here.

class Session(models.Model):
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=100)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='sessions')