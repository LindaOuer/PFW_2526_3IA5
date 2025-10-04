from django.contrib import admin
from .models import *

# Register your models here.
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'start_date', 'end_date')
    search_fields = ('name', 'location', 'theme')
    list_filter = ('theme', 'location')
    list_per_page = 1

admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Submission)
admin.site.register(OrganizingCommittee)
