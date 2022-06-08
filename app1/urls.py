from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    
    path('',index_view,name='index_view'),
    path('create_company',create_company,name='create_company'),



]