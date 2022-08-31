from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('add/challenge',views.add_challenge),
    path('add/challenges',views.show_challenge),
    path('submit_flag',views.submit_flag)
    # path(r'^$',TemplateView.as.views(template_name='login.html')
]