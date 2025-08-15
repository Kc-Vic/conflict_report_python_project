"""

This file contains URL patterns for the civ_intel application.
It maps URLs to views for handling reports and comments.


"""

from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReportAboutView.as_view(), name='home'),
    path('report_add/', views.report_add, name='report_add'),
    path('report_edit/<slug:slug>/', views.report_edit, name='report_edit'),
    path('report_delete/<slug:slug>/', views.report_delete, name='report_delete'),
    path('report_list/', views.ReportFeedView.as_view(), name='feed'),
    path('<slug:slug>/', views.report_detail, name='report_detail'),
    
]