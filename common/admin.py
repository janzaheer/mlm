from django.contrib import admin

from .models import UserProfile, Partner, Member


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'mobile', 'gender',)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'mobile', 'gender', 'user', 'created_user', 'step_id')


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'member_child', 'position')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Member, MemberAdmin)
