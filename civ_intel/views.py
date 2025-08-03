from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def report_feed(request):
    return HttpResponse("Hello, this is the feed page of the civ_intel app.")