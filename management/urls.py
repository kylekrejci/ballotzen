from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'management'

urlpatterns = [
    path('management_login/', auth_views.LoginView.as_view(), name='management_login'),
    path('management_logout/', auth_views.LogoutView.as_view(), name='management_logout'),
    path('console/', views.dashboard, name='dashboard')
    ]