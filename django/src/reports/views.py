from django.shortcuts import render
from profiles.models import Profile
from reports.models import Report
from reports.forms import ReportForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from reports.utils import get_report_image


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
        
        

        
    
