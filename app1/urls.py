from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('', index_view, name='index_view'),
    path('create_company', create_company, name='create_company'),
    path('Company_Features/', Company_Features, name='Company_Features'),
    path('Company_Features_Save/<int:pk>',Company_Features_Save, name='Company_Features_Save'),
    path('gst_details',gst_details,name='gst_details'),
    path('selected_companies/<int:pk>',selected_companies,name='selected_companies'),
    path('shut_company/<int:pk>',shut_company,name='shut_company'),
    path('alter_company/<int:pk>',alter_company,name='alter_company'),
    path('create_group',create_group,name="create_group"),
    

    
    




]
