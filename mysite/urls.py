"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from rsvp import views

urlpatterns = [
	path('',views.index),
	path('login',views.user_login),
	path('logout',views.user_logout),
	path('register_page',views.register_page),
	path('register',views.register),
	path('main',views.main_page),
	path('createEvent',views.create_event),
    path('admin/', admin.site.urls),
]
