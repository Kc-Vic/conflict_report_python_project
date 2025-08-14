from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Report
from .forms import CommentForm

# Create your views here.

class ReportAboutView(generic.TemplateView):
    template_name = 'civ_intel/about.html'

class ReportFeedView(generic.ListView):
   queryset = Report.objects.all().order_by('-created_at')
   template_name = 'civ_intel/index.html'
   paginate_by = 3

def report_detail(request, slug):
   queryset = Report.objects
   report = get_object_or_404(queryset, slug=slug)
   comments = report.comments.all().order_by('-created_at')
   comment_count = report.comments.count()
   if request.method == "POST":
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.report = report
        comment.save()
        messages.add_message(
            request, messages.SUCCESS, "Your post has been submitted"
        )
   comment_form = CommentForm()


   return render(
      request, 'civ_intel/report_detail.html', 
      {
         'report': report,
         'comments': comments,
         'comment_count': comment_count,
         'comment_form': comment_form,
      },
   )