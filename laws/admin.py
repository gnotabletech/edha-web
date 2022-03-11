from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from .models import BillsAndLaws, AdminInfo


class BillsAndLawsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'short_title']
    fields = ['title', 'short_title', 'stage_key', 'sponsor', 'first_reading', 'second_reading', 'committee_date', 'referred_committee', 'third_reading', 'assent_date', 'document']
    list_filter = ['stage_key', 'assent_date', ('assent_date', DateRangeFilter)]
    list_display = ['title', 'stage_key', 'assent_date']


# Register your models here.
admin.site.register(BillsAndLaws, BillsAndLawsAdmin)
admin.site.register(AdminInfo)
