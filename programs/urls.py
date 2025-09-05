from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('programs/', views.program_list, name='program_list'),
    path('programs/<int:pk>/', views.program_detail, name='program_detail'),
]