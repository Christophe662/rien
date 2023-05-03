from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path ('',views.mycv_view,name='my_cv'),

    
]