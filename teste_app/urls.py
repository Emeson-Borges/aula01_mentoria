
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.sua_view, name='index'),
]


