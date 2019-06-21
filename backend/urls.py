from django.urls import path
from django.conf.urls import url

from .djangoapps.sample import views as SampleViews
from .djangoapps.login import views as LoginViews
from .djangoapps.index import views as IndexViews

urlpatterns = [
    path('sample', SampleViews.sample, name='sample'),
    path('login', LoginViews.login, name='login'),

    path('', IndexViews.index, name='index'),
    path('api_getProName', IndexViews.api_getProName, name='api_getProName'),
    path('api_getCourse', IndexViews.api_getCourse, name='api_getCourse'),
    path('api_getClass', IndexViews.api_getClass, name='api_getClass'),
    path('api_getProList', IndexViews.api_getProList, name='api_getProList'),
    path('api_getTime', IndexViews.api_getTime, name='api_getTime'),
    path('api_getCheck', IndexViews.api_getCheck, name='api_getCheck'),
    path('api_getWeek', IndexViews.api_getWeek, name='api_getWeek'),
    path('api_getTwoTab', IndexViews.api_getTwoTab, name='api_getTwoTab'),
    path('api_getFourTab', IndexViews.api_getFourTab, name='api_getFourTab'),
    path('api_saveData', IndexViews.api_saveData, name='api_saveData'),
]
