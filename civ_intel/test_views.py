from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import Report, Comment

class ReportViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_report_list_view(self):
        response = self.client.get(reverse('report_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'civ_intel/report_list.html')

    def test_report_detail_view(self):
        report = Report.objects.create(
            title='Test Report',
            content='This is a test report.',
            author=self.user
        )
        response = self.client.get(reverse('report_detail', args=[report.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'civ_intel/report_detail.html')

    def test_report_add_view(self):
        response = self.client.get(reverse('report_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'civ_intel/report_add.html')

        response = self.client.post(reverse('report_add'), {
            'title': 'New Report',
            'content': 'This is a new report.',
            'location': None,
            'anonymous': False
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful form submission

    