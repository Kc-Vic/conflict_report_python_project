from django.db import models
from django.contrib.auth.models import User

# Define the status choices for the report
STATUS = (
    (0, "Draft"),
    (1, "Published"),
    (2, "Approved"),
)

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reports"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(
        max_length=100, help_text="State where the report is filed"
    )
    status = models.IntegerField(choices=STATUS, default=0)
    anonymous = models.BooleanField(
        default=False,
        help_text="If checked, the report will be anonymous"
    )
    attachment = models.FileField(
        upload_to='attachments/', 
        null=True, 
        blank=True
    )