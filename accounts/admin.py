from django.contrib import admin

# Register your models here.


from accounts.models import UserProfile




class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'name', 'surname', 'address')


admin.site.register(UserProfile, UserProfileAdmin)
