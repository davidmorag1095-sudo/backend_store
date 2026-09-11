from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home_product'),
    path('api/all/', views.api_category, name='api_category'),
]
