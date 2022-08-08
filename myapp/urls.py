from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('api', views.api),
    path('api2', views.api2),
    path('html', views.html),
]