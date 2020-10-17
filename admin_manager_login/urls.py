"""admin_manager_login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app1 import views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html')),
    # path('', views.showindex,name='showindex'),
    path('admin_login/', views.admin_login,name='admin_login'),
    path('admin_login_details/', views.admin_login_details,name='admin_login_details'),
    path('admin_registration/', views.admin_register,name='admin_register'),
    path('admin_register_details/', views.admin_register_details,name='admin_register_details'),
    path('sbi/', views.sbi_branch,name='sbi_branch'),
    path('icici/', views.icici_branch,name='icici_branch'),
    path('sbi_manager/', views.manager_login,name='manager_login'),
    path('sbi_manager_login_details/', views.manager_login_details,name='manager_login_details'),
    path('icici_manager/', views.icici_manager,name='icici_manager'),
    path('icici_manager_login/', views.icici_manager_login,name='icici_manager_login'),
    path('icici_manager_registration/', views.icici_manager_registration,name='icici_manager_registration'),
    path('icici_manager_register_details/', views.icici_manager_register_details,name='icici_manager_register_details'),
    path('manager/', views.brach_managers,name='brach_managers'),
    path('manager_registration/', views.manager_registration,name='manager_registration'),
    path('manager_register_details/', views.manager_register_details,name='manager_register_details'),
]
