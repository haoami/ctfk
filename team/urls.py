from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('registerteam',views.registerteam),
    path('get_team_data',views.get_team_data),
    path('jointeam',views.join_team),
    path('auth/delete',views.delete_team),
    path('myteam',views.my_team),
    path('lookteam',views.look_team),
    path('deleteuser',views.leave_team)
    # path('auth/login',views.login)
    # path(r'^$',TemplateView.as.views(template_name='login.html')
]
