from django.contrib import admin

from .models import UserProfile, Partner


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'mobile', 'gender',)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'partner_user', 'position')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Partner, PartnerAdmin)
