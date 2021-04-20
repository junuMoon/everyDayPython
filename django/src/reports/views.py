from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.views.generic import DetailView, ListView, TemplateView
from profiles.models import Profile

from xhtml2pdf import pisa

from reports.forms import ReportForm
from reports.models import Report
from reports.utils import get_report_image


class ReportListView(ListView):
    model = Report
    template_name = 'reports/main.html'
        
class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/detail.html'

class UploadTemplateView(TemplateView):
    template_name = 'reports/from_file.html'
    
def csv_upload_view(request):
    return HttpResponse()

# Create your views here.
def create_report_view(request):
    form = ReportForm(request.POST or None)
    if request.is_ajax():
        image = request.POST.get('image')
        img = get_report_image(image)
        author_user = User.objects.get(username='test_user')
        author_profile = Profile.objects.get(user=author_user) #TODO: need proper user input
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.image = img
            instance.author = author_profile
        instance.save()

        return JsonResponse({'msg': 'success'})
    return JsonResponse({})
        
def render_pdf_view(request, pk):
    template_path = 'reports/pdf.html'
    obj = get_object_or_404(Report, pk=pk)
    context = {'obj': obj}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
        

        
    
