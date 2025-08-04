from django.contrib import admin
from civ_intel.models import Report, Comment
from civ_intel.models import State

# Register your models here.
admin.site.register(Report)
admin.site.register(State)
admin.site.register(Comment)