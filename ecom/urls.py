from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name="home"),
    path('removepunc/', views.removepunc, name="removepunc"),
    path('index/', views.index, name="index"),


]
