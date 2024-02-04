
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('drugs/', views.drugs_view),
    path('drugs/<int:id>', views.drugs_view),
]
