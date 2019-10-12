from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('about/', views.about, name='about'),
]
