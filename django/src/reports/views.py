from django.shortcuts import render
from profiles.models import Profile
from reports.models import Report
from django.http import JsonResponse
from django.contrib.auth.models import User


# Create your views here.
def create_report_view(request):
    if request.is_ajax():
        name = request.POST.get('name')
        remarks = request.POST.get('remarks')
        img = request.POST.get('image') # TODO: from .utils import get_report_image
        
        author_user = User.objects.get(username='test_user')
        author_profile = Profile.objects.get(user=author_user) #TODO: need proper user input
        
        report = Report(
            name = name,
            image = img,
            remarks = remarks,
            author = author_profile
        )
        report.save()
        return JsonResponse({'msg': 'success'})
    return JsonResponse({})
        
        

        
    
