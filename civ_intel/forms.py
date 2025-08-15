"""

This file contains forms for the civ_intel application.
It defines forms for creating and editing reports and comments.

"""

from .models import Comment, Report
from django import forms

"""
The comment form is used to create a new comment on a report by calling the save method.
The report form is used to create a new report or edit an existing one.
It includes fields for the report title, content, location, and whether it is anonymous..

"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'content', 'location', 'anonymous']