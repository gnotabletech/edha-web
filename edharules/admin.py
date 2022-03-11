from django.contrib import admin
from .models import EDHARule


class EDHARuleAdmin(admin.ModelAdmin):
    search_fields = ['rule_section_title', 'rule_subsection_title', 'rule_details']


# Register your models here.
admin.site.register(EDHARule)
