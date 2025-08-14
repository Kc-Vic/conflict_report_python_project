from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReportAboutView.as_view(), name='home'),
    path('report_list/', views.ReportFeedView.as_view(), name='feed'),
    path('<slug:slug>/', views.report_detail, name='report_detail'),
]