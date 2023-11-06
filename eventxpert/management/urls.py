from django.urls import path
from . import views
from django.views.generic import RedirectView
from .views import register_for_event
urlpatterns = [
    path('student/', views.event_list_view, name = 'event'),
    path('category/',views.CategoryListView.as_view(), name='category')
]
urlpatterns += [
    path('category/create/', views.CategoryCreate.as_view(), name='category-create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category-delete'),
]
urlpatterns +=[
    path('host/create_event', views.organisation_form_view, name = 'create-event'),
    path('host/detail/', views.event_list_view),
    path('student/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('student/<int:event_id>/register/', register_for_event, name='register-for-event'),
    path('host/event/detailed_view', views.host_event_detailed_view, name="host_event_detailed_view"),



    path('student/', views.student, name = 'student'),
    path('host/', views.host, name = 'host'),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("login/student", views.student_login, name="student_login"),
    path("login/host", views.host_login, name="host_login"),
    path("permission_denied", views.permission_denied, name="permission_denied"),
    path('', views.login, name="login" ),
]
