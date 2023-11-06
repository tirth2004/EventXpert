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
from django.views import generic
from django.urls import reverse
from .models import TestModel,Category,OrganisationEvent,Student
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.http import HttpResponse

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



class CategoryListView(generic.ListView):
    model= Category
    context_object_name='category_list'
    template_name='category.html'

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from management.models import Category

class CategoryCreate(CreateView):
    model = Category
    fields = ['category_name']
    def get_success_url(self):
        return reverse_lazy('category') 

class CategoryUpdate(UpdateView):
    model = Category
    fields = ['category_name']

class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category')

from django.shortcuts import render
from .forms import OrganisationEventForm

def organisation_form_view(request):
    if request.method == 'POST':
        form = OrganisationEventForm(request.POST)
        if form.is_valid():
            # Process the form data (save, etc.) as needed
            form.save()
            # Redirect to a success URL or another view
    else:
        form = OrganisationEventForm()

    return render(request, 'eventform.html', {'form': form})

def event_list_view(request):
    events = OrganisationEvent.objects.all()  # Fetch all events from the database
    return render(request, 'event_list.html', {'events': events})

class EventDetailView(generic.DetailView):
    model = OrganisationEvent
    template_name = 'event_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        context['registered_students_count'] = event.registered_students
        return context
    
def register_for_event(request, event_id):
    if request.user.is_authenticated:
        event = get_object_or_404(OrganisationEvent, pk=event_id)
        student = get_object_or_404(Student, user=request.user)
        # Logic to send student details to the admin (not implemented in this example)
        return HttpResponse("Registration successful!")
    else:
        return HttpResponse("You need to be logged in to register.")
# def registration_success(request):
#     return render(request, 'registration_success.html')

# class EventDetailView(generic.DetailView):
#     model=OrganisationEvent
#     template_name='event_details.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     event = self.get_object()
    #     context['registered_students_count'] = event.registered_students
    #     return context
    
    

    # def post(self, request, pk):
    #     # Logic for student registration (not implemented in this example)
    #     student = get_object_or_404(Student, user=request.user)
    #     event = get_object_or_404(OrganisationEvent, pk=pk)
    #     student.register_for_event(event)
    #     messages.success(request, 'Thank you for registering!') 
    #     return redirect('registration/success/', pk=pk)





    

