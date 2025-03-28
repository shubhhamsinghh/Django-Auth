from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest

@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_d = {'username':'','password1':'','password2':''}
        form = UserCreationForm(initial=initial_d)
    return render(request,'auth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_d = {'username':'','password':''}
        form = AuthenticationForm(initial=initial_d)
    return render(request,'auth/login.html',{'form':form})

@auth
def dashboard_view(request):
    return render(request,'pages/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')