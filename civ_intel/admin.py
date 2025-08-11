from django.contrib import admin
from civ_intel.models import Report, Comment
from civ_intel.models import State
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Report)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(State)
admin.site.register(Comment)