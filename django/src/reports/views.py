import csv
from datetime import datetime
from os import read

from customers.models import Customer
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.views.generic import DetailView, ListView, TemplateView
from products.models import Product
from profiles.models import Profile
from sales.models import CSV, Position, Sale
from xhtml2pdf import pisa

from reports.forms import ReportForm
from reports.models import Report
from reports.utils import get_report_image

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'reports/main.html'
        
class ReportDetailView(LoginRequiredMixin,DetailView):
    model = Report
    template_name = 'reports/detail.html'

class UploadTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'reports/from_file.html'

@login_required
def csv_upload_view(request):
    if request.method == 'POST':
        csv_file_name = request.FILES.get('file').name
        csv_file = request.FILES.get('file')
        obj, created = CSV.objects.get_or_create(file_name=csv_file_name)
        
        if created:
            obj.csv_file = csv_file
            obj.save()
            
            with open(obj.csv_file .path, 'r') as f:
                reader = csv.reader(f)
                reader.__next__() # skip the first row
                for row in reader:
                    transaction_id = row[1].strip()
                    product = row[2].strip()
                    quantity = int(row[3])
                    customer = row[4].strip()
                    date = parse_date(row[5].strip())
                    date = datetime.combine(date, datetime.min.time())   
                    
                    try:
                        product_obj = Product.objects.get(name__iexact=product)
                    except Product.DoesNotExist:
                        product_obj = None
                    
                    if product_obj is not None:
                        customer_obj, _ = Customer.objects.get_or_create(name=customer)
                        salesman_obj = Profile.objects.get(user=request.user)
                        position_obj, _ = Position.objects.get_or_create(product=product_obj,
                                                                        quantity=quantity,
                                                                        created=date)
                        sale_obj, _ = Sale.objects.get_or_create(transaction_id=transaction_id,
                                                                defaults={
                                                                    'customer': customer_obj,
                                                                    'salesman': salesman_obj,
                                                                    'created': date})
                        sale_obj.positions.add(position_obj)
                        sale_obj.save()
                        
                    return JsonResponse({'ex': False})
        else:
            return JsonResponse({'ex': True})
    return HttpResponse()

@login_required
def create_report_view(request):
    form = ReportForm(request.POST or None)
    if request.is_ajax():
        image = request.POST.get('image')
        img = get_report_image(image)
        author_profile = Profile.objects.get(user=request.user)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.image = img
            instance.author = author_profile
        instance.save()

        return JsonResponse({'msg': 'success'})
    return JsonResponse({})
        
@login_required
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
    html = template.render(context) #FIXME: error occured

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
        

        
    
