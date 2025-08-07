from . import views
from django.urls import path

urlpatterns = [
    path("", views.ReportListView.as_view(), name="home"),
]