from django.urls import path
from .views import addBook, getbooks

urlpatterns = [
    path('addbook/', addBook),
    path('getbooks/', getbooks),
    
]