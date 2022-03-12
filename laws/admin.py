from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from .models import BillsAndLaws, AdminInfo


@admin.action(description='Mark selected laws as assented to')
def assent(modeladmin, request, queryset):
    queryset.update(stage_key='STAGE7')


class BillsAndLawsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'short_title']
    fields = ['title', 'short_title', 'stage_key', 'sponsor', 'first_reading', 'second_reading', 'committee_date',
              'referred_committee', 'third_reading', 'assent_date', 'document']
    list_filter = ['stage_key', 'assent_date', ('assent_date', DateRangeFilter)]
    list_display = ['title', 'stage_key', 'assent_date']
    actions = [assent]


# Register your models here.
admin.site.register(BillsAndLaws, BillsAndLawsAdmin)
admin.site.register(AdminInfo)
