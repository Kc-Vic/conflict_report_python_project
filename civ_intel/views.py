from django.shortcuts import render
from django.views import generic
from .models import Report

# Create your views here.

class ReportFeedView(generic.ListView):
   queryset = Report.objects.all()
   template_name = 'civ_intel/report_list.html'