# api/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blog, Category ,Comment, Like ,Dislike


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_staff', 'profile_image', 'bio', 'about', 'phone_number')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
         'fields': ('profile_image', 'bio', 'about', 'phone_number')}),
    )
    # Remove date_joined from list_display
    list_display = [field for field in list_display if field != 'date_joined']


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)
