from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('login',
         TemplateView.as_view(template_name='login/login.html'),
         name='login'),

    path('', views.index, name='index'),
    path('api_getProName/<str:pro_num>', views.api_getProName, name='api_getProName'),
    path('api_getCourse', views.api_getCourse, name='api_getCourse'),
    path('api_getClass/<str:course_id>', views.api_getClass, name='api_getClass'),
    path('api_getProList/<int:class_id>', views.api_getProList, name='api_getProList'),
    path('api_getTime/<int:class_id>', views.api_getTime, name='api_getTime'),
    path('api_getCheck/<int:class_id>', views.api_getCheck, name='api_getCheck'),
    path('api_getWeek/<int:class_id>', views.api_getWeek, name='api_getWeek'),
    path('api_getTwoTab/<int:class_id>', views.api_getTwoTab, name='api_getTwoTab'),
    path('api_getFourTab/<int:class_id>', views.api_getFourTab, name='api_getFourTab'),
    path('api_saveData', views.api_saveData, name='api_saveData'),
]
