from django.contrib import admin
from django.urls import path
from .views import *
app_name="tech"
urlpatterns = [
    path('', HomeView.as_view(),name="home"),
    path('post/<slug>', SingleView.as_view(), name="single"),
]
