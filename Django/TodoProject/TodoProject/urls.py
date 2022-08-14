"""TodoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from argparse import Namespace
from django.contrib import admin
from django.urls import path
from django.views import View
from TODO.views import StudentCreate, StudentListView, StudentDetailView
from TODO.views import StudentUpdateView, StudentDeleteView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentCreate.as_view()),
    path('list/', StudentListView.as_view()),
    path('details/<pk>/', StudentDetailView.as_view()),
    path('update/<pk>/', StudentUpdateView.as_view()),
    path('delete/<pk>/', StudentDeleteView.as_view()),
    path('details/<pk>/list/', StudentListView.as_view()),

]
