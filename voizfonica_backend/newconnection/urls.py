from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('new/',views.conn, name="new"),
    path('new/',views.portin, name="new")
]