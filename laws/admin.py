from django.contrib import admin
from .models import BillsAndLaws, AdminInfo


class BillsAndLawsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'short_title']


# Register your models here.
admin.site.register(BillsAndLaws, BillsAndLawsAdmin)
admin.site.register(AdminInfo)
