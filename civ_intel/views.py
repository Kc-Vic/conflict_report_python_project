from django.shortcuts import render
from django.views import generic
from .models import Report


# Create your views here.
class ReportListView(generic.ListView):
    queryset = Report.objects.all()
    template_name = 'feed_list.html'