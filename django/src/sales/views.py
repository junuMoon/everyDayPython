from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sales.models import Sale
from sales.forms import SalesSearchForm

# Create your views here.

def home_view(request):
    form = SalesSearchForm(request.POST or None)
    
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(date_from, date_to, chart_type)
    context = {
        'form': form
    }
    return render(request, template_name='sales/home.html', context=context)

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sales'  # replace object_list

# def sale_list_view(request):
#     qs = Sale.objects.all()
#     return render(request, 'sales/main.html', {'object_list':qs})

# class SaleDetailView(DetailView):
#     model = Sale
#     template_name = 'sales/detail.html'
    
def sale_detail_view(request, **kwargs):
    print(type(request))
    pk = kwargs.get('pk')
    obj = Sale.objects.get(pk=pk)
    return render(request, 'sales/detail.html', {'object':obj})
