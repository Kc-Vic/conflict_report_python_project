from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReportFeedView.as_view(), name='home'),
    path('<slug:slug>/', views.report_detail, name='report_detail'),
]