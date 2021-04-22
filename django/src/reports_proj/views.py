from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    error_msg = None
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('sales:home')
        else:
            error_msg = 'Error occurred'
    context = {
        'form': form,
        'error_msg': error_msg
    }
    
    return render(request, 'auth.html', context=context)

            