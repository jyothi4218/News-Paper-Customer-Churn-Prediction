from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
admin.site.unregister(User)  # Optional: unregister default if you want customization
admin.site.register(User, UserAdmin)
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'gender', 'reason_for_switch')


