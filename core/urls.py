from django.urls import path
from . import views

urlpatterns = [
    path('test-f/', views.test_api, name='test-f'),
    path('test-c/', views.TestAPI.as_view(), name='test-c'),
]