from django.contrib import admin
from .models import BillsAndLaws, AdminInfo


class BillsAndLawsAdmin(admin.ModelAdmin):
    search_fields = ['TITLE', 'SHORT_TITLE']


# Register your models here.
admin.site.register(BillsAndLaws, BillsAndLawsAdmin)
admin.site.register(AdminInfo)
