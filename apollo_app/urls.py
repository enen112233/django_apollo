
from django.urls import path

from apollo_app import views

urlpatterns = [
    path('index/',views.index),
    path('login/', views.login),
    path('safe/',views.safeA),
    path('safe/',views.safeA),
    path('login/', views.login),
    path('safe_b/', views.safe_b),
]






