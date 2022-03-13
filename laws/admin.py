from django.contrib import admin, messages
from django.utils.translation import ngettext
from rangefilter.filters import DateRangeFilter

from .models import BillsAndLaws, AdminInfo


class BillsAndLawsAdmin(admin.ModelAdmin):
    @admin.action(description='Mark selected laws as assented to')
    def assent(self, request, queryset):
        updated = queryset.update(stage_key='STAGE7')
        self.message_user(request, ngettext(
            '%d law was successfully marked as assented to.',
            '%d laws were successfully marked as assented to.',
            updated,) % updated, messages.SUCCESS)

    search_fields = ['title', 'short_title']
    fields = ['title', 'short_title', 'stage_key', 'sponsor', 'first_reading', 'second_reading', 'committee_date',
              'referred_committee', 'third_reading', 'assent_date', 'document']
    list_filter = ['stage_key', 'assent_date', ('assent_date', DateRangeFilter)]
    list_display = ['title', 'short_title', 'stage_key', 'assent_date']
    actions = [assent]


# Register your models here.
admin.site.register(BillsAndLaws, BillsAndLawsAdmin)
admin.site.register(AdminInfo)
