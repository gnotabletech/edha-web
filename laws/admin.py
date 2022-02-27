from django.contrib import admin
from .models import BillsAndLaws, AdminInfo

# Register your models here.
admin.site.register(BillsAndLaws)
admin.site.register(AdminInfo)
