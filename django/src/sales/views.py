from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sales.models import Sale

# Create your views here.

def home_view(request):
    hello = 'hello world from the view'
    return render(request, template_name='sales/home.html', context={'hello': hello})

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sales'  # replace object_list

# def sale_list_view(request):
#     qs = Sale.objects.all()
#     return render(request, 'sales/main.html', {'objecdt_list':qs})

# class SaleDetailView(DetailView):
#     model = Sale
#     template_name = 'sales/detail.html'
    
def sale_detail_view(request, **kwargs):
    print(type(request))
    pk = kwargs.get('pk')
    obj = Sale.objects.get(pk=pk)
    return render(request, 'sales/detail.html', {'object':obj})
