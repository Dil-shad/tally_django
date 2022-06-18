from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(GroupModel)
admin.site.register(LedgerModel)
admin.site.register(CompanyModel)
admin.site.register(StockGroupModel)