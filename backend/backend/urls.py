from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from taskmanager import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
