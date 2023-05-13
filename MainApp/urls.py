from . import views
from django.contrib import admin
from django.urls import include, path

app_name = 'MainApp'

urlpatterns = [
    path('', views.main, name='main'),
]
