from .views import *
from django.urls import path

urlpatterns = [
    path('', simple_view, name='conference_simple_view'),
    path('home/', home_view, name='conference_home'),
    path('welcome/<str:name>/', welcome, name='conference_welcome'),
    path('list/', listConferences, name='conference_list'),
    path('listLV/', ConferenceListView.as_view(), name='conference_list_view'),
]
