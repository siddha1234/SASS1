from django import views
from django.urls import path
from . import views


urlpatterns= [
     
    path('about', views.about),
    path('buy', views.buy), 
    path('contact', views.contact),
    path('medicine', views.medicine), 
    path('news',views.news),
    path('',views.index),
]