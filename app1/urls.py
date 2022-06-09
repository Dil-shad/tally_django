from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('', index_view, name='index_view'),
    path('create_company', create_company, name='create_company'),
    path('Company_Features/', Company_Features, name='Company_Features'),
    path('Company_Features_Save/<int:pk>',Company_Features_Save, name='Company_Features_Save'),
    path('Gst_Details',Gst_Details,name='Gst_Details'),




]
