from django.shortcuts import render, get_object_or_404
from django.views import generic
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

def add_comment(request):
   if request.method == 'POST':
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
         comment = comment_form.save(commit=False)
         comment.author = request.user
         report_slug = request.POST.get('report_slug')
         report = get_object_or_404(Report, slug=report_slug)
         comment.report = report
         comment.save()
         return redirect('report_detail', slug=report.slug)
   else:
      comment_form = CommentForm()

   return render(request, 'civ_intel/add_comment.html', {'comment_form': comment_form})