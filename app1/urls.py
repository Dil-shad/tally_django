from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('', index_view, name='index_view'),
    path('create_company', create_company, name='create_company'),
    path('Company_Features/', Company_Features, name='Company_Features'),
    path('Company_Features_Save/<int:pk>',
         Company_Features_Save, name='Company_Features_Save'),
    path('gst_details', gst_details, name='gst_details'),
    path('selected_companies/<int:pk>',
         selected_companies, name='selected_companies'),
    path('shut_company/<int:pk>', shut_company, name='shut_company'),
    path('alter_company/<int:pk>', alter_company, name='alter_company'),
    path('create_group', create_group, name="create_group"),
    path('create_ledger', create_ledger, name='create_ledger'),
    path('log_company/<int:pk>', log_company, name='log_company'),
    path('create_voucher', create_voucher, name='create_voucher'),
    path('create_currency', create_currency, name='create_currency'),
    path('stock_group', stock_group, name='stock_group'),
    path('stock_category', stock_category, name='stock_category'),
    path('stock_item', stock_item, name='stock_item'),
    path('unit_creation', unit_creation, name='unit_creation'),
    path('stock_location', stock_location, name='stock_location'),
    path('Employee-Grp-Creation',EmployeeGroupCreation,name='EmployeeGroupCreation'),
    path('PayrollEmployee',PayrollEmployee,name='PayrollEmployee'),
    path('Units_work',Units_work,name='Units_work'),
    path('Attendence_work',Attendence_work,name='Attendence_work'),
    path('payheadfun',payheadfun,name='payheadfun'),













]
