"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts import views

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'), 
    path('', views.CustomLoginView.as_view(), name='home_login'),
    path('logout/', views.custom_logout , name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('distributor-dashboard/', views.distributor_dashboard, name='distributor_dashboard'),
    path('forgot-password/', views.password_reset_request, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('set-new-password/', views.set_new_password, name='set_new_password'),
]
