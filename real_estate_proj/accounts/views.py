from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        # register users:

        messages.error(request, 'Testing error Message')
        return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # login users:  
        return 
        
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect(request, 'index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')