from django.urls import path
from . import views

urlpatterns = [
    path('professors/', views.professor_list),
    path('professors/<int:professor_pk>/courses/', views.course_list),
    path('courses/<int:course_pk>/classes/', views.class_list),
    path('classes/<int:pk>/', views.class_detail),
]

