from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.properties, name='properties'),
    # Dynamic URL path that accepts the house ID number (e.g., /property/1/)
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('philosophies/', views.philosophies, name='philosophies'),
    path('contact/', views.contact, name='contact'),
]