from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('student/', views.student, name = 'student'),
    path('host/', views.host, name = 'host'),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("login/student", views.student_login, name="student_login"),
    path("login/host", views.host_login, name="host_login"),
    path("permission_denied", views.permission_denied, name="permission_denied"),
    path('', views.login, name="login" ),
]
