from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import RegistrationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import StudentLoginForm,HostLoginForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import Group

# Create your views here.
def student(request):
    context = {}
    return render(request, 'student.html', context=context)

def host(request):
    context = {}
    return render(request, 'host.html', context=context)

def permission_denied(request):
    context={}
    return render(request, 'permission_denied.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    context = {}
    return render(request, "login.html", context = context)

def student_login(request):
    context= {}
    return render(request, "student_login.html", context=context)

def host_login(request):
    return render(request, 'host_login.html')



def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)    
                return redirect('student')
    else:
        form = StudentLoginForm()
    return render(request, 'student_login.html', {'form': form})

# def host_login(request):
#     if request.method == 'POST':
#         form = HostLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 auth_login(request, user)    
#                 return redirect('host')
#     else:
#         form = HostLoginForm()
#     return render(request, 'host_login.html', {'form': form})



def host_login(request):
    if request.method == 'POST':
        form = HostLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                host_group = Group.objects.get(name='Host')  # Get the "Host" group
                if host_group in user.groups.all():
                    # User is in the "Host" group, redirect to "host.html"
                    return redirect('host')
                else:
                    # User is not in the "Host" group, redirect to "permission_denied"
                    return redirect('permission_denied')
    else:
        form = HostLoginForm()
    return render(request, 'host_login.html', {'form': form})




