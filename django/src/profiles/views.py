from django.shortcuts import render
from django.contrib.auth.models import User
from profiles.models import Profile
from profiles.forms import ProfileForm
# Create your views here.

def my_profile_view(request):
    profile = Profile.objects.get(user=request.user) 
    print(request.POST)
    print(request.FILES)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False
    
    if request.method == "POST":
        if form.is_valid:
            form.save()
            confirm = True
    
    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
    }
    return render(request, 'profiles/main.html', context) 
