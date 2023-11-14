from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import GetStatEmployee, GetStatClient

router = routers.DefaultRouter()

router.register(r'employee', GetStatEmployee, basename='employee')
router.register(r'client', GetStatClient, basename='client')

urlpatterns = [
    path('', include(router.urls)),
    # path('client/<int:client_id>/', GetStatClient.as_view()),
]
