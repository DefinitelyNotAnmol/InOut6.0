from django.urls import path, include
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.pay)
]
