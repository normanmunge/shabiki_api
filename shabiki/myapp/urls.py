from django.urls import path
from . import views;

urlpatterns = [
    path('home/', views.home),
    path('getuser/<name>/<int:id>', views.getuser),
    path('getuserqryview', views.getuserqryview),
    path('showform/', views.showform, name="showform"),
    path('getform/', views.getform, name="getform"),
    path('getuserform/', view=views.getuserform, name="getuserform")
]