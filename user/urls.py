from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('auth/register',views.register),
    path('auth/login',views.login),
    path('get_user',views.getuser),
    path('get_users',views.get_users),
    path('delete_users',views.delete_user)
    # path(r'^$',TemplateView.as.views(template_name='login.html')
]