from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from landing.models import MemberInfo, StaffInfo


class MemberInfoAdmin(admin.ModelAdmin):
    search_fields = ['username', 'lastname', 'firstname', 'constituency', 'lga']
    readonly_fields = ['constituency', 'lga', 'position_key']
    ordering = ['constituency']
    fields = ['firstname', 'othernames', 'lastname', 'username', 'constituency', 'lga', 'position_key', 'qualifications',
              'date_of_birth', 'age', 'profile_description', 'tenure', 'party', 'tenure_start', 'email', 'projects',
              'status', 'committee_key', 'twitter_account', 'facebook_account', 'instagram_account', 'linkedin_account',
              'phone', 'profile_image', 'public_image', 'cover_image']

    def has_add_permission(self, request, obj=None):
        return False


class StaffInfoAdmin(admin.ModelAdmin):
    search_fields = ['username', 'surname', 'firstname', 'designation']


# Register your models here.
admin.site.register(StaffInfo, StaffInfoAdmin)
admin.site.register(MemberInfo, MemberInfoAdmin)
