from django.shortcuts import render
from profiles.models import Profile
from reports.models import Report
from django.http import JsonResponse
from django.contrib.auth.models import User
from reports.utils import get_report_image


# Create your views here.
def create_report_view(request):
    if request.is_ajax():
        name = request.POST.get('name')
        remarks = request.POST.get('remarks')
        image = request.POST.get('image')
        
        img = get_report_image(image)
        
        author_user = User.objects.get(username='test_user')
        author_profile = Profile.objects.get(user=author_user) #TODO: need proper user input
        
        Report.objects.create(
            name = name,
            image = img,
            remarks = remarks,
            author = author_profile
        )

        return JsonResponse({'msg': 'success'})
    return JsonResponse({})
        
        

        
    
