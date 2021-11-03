from django.shortcuts import redirect, render

# Create your views here.

def register(request):
    if request.method == 'POST':
        # register users:
        return   

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