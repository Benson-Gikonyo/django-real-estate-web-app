from django.shortcuts import redirect, render

# Create your views here.

def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')