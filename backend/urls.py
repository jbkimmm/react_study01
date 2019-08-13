from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('login',
         TemplateView.as_view(template_name='login/login.html'),
         name='login'),

    path('', views.index, name='index'),
    path('api_getProName', views.api_getProName, name='api_getProName'),
    path('api_getCourse', views.api_getCourse, name='api_getCourse'),
    path('api_getClass', views.api_getClass, name='api_getClass'),
    path('api_getProList', views.api_getProList, name='api_getProList'),
    path('api_getTime', views.api_getTime, name='api_getTime'),
    path('api_getCheck', views.api_getCheck, name='api_getCheck'),
    path('api_getWeek', views.api_getWeek, name='api_getWeek'),
    path('api_getTwoTab', views.api_getTwoTab, name='api_getTwoTab'),
    path('api_getFourTab', views.api_getFourTab, name='api_getFourTab'),
    path('api_saveData', views.api_saveData, name='api_saveData'),
]
