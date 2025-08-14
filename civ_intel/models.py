from django.db import models
from django.utils.text import slugify
import uuid
from django.contrib.auth.models import User

# Define the status choices for the report
STATUS = (
    (0, "Draft"),
    (1, "Published"),
    (2, "Approved"),
)

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class State(models.Model):
    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=10, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "States"

    def __str__(self):
        return self.name


class Report(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reports"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(
        State,
        on_delete=models.RESTRICT,
        related_name="state_reports",
        null=True,
        blank=True,
        help_text="Select the state where the incident occurred"
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
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.title} {self.author}"
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + "-" + str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)

class Comment(models.Model):
    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"Comment by {self.author.username} on {self.report.title} {self.comment}"