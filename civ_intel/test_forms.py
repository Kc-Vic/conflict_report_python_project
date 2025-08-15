from django.test import TestCase
from .forms import CommentForm, ReportForm

# Test for CommentForm
class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'comment': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Form is valid')

# Test for ReportForm
class TestReportForm(TestCase):

    def test_form_is_valid(self):
        report_form = ReportForm({
            'title': 'Test Report',
            'content': 'This is a test report content.',
        })
        self.assertTrue(report_form.is_valid(), msg='Form is valid')

    def test_form_is_not_valid(self):
        report_form = ReportForm({
            'title': '',
            'content': 'Test content without a title.',
        })
        self.assertTrue(report_form.is_valid(), msg='Form is valid')
        self.assertIn('title', report_form.errors, msg='Title field is required')
    
