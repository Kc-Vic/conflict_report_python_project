from .models import Comment, Report
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'content', 'location', 'anonymous', 'status']