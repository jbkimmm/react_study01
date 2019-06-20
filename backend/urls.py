from django.urls import path
from django.conf.urls import url

from .djangoapps.sample import views as SampleViews
from .djangoapps.login import views as LoginViews
from .djangoapps.index import views as IndexViews

urlpatterns = [
    path('sample', SampleViews.sample, name='sample'),
    path('login', LoginViews.login, name='login'),
    path('', IndexViews.index, name='index'),
]
