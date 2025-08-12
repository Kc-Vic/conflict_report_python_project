from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Report

# Create your views here.
class ReportFeedView(generic.ListView):
   queryset = Report.objects.all().order_by('-created_at')
   template_name = 'civ_intel/index.html'
   paginate_by = 3

def report_detail(request, slug):
   queryset = Report.objects
   report = get_object_or_404(queryset, slug=slug)

   return render(request, 'civ_intel/report_detail.html', {'report': report},)