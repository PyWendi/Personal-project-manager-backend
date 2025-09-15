from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .model_classes.customuser import CustomUser


class CustomUserAdmin(UserAdmin):
    # Customize the fields displayed in the list view
    list_display = ('email', 'first_name', 'subscribe_type', 'is_staff', 'is_superuser',)
    readonly_fields = ("date_joined",)
    # Customize the fields displayed in the add/edit forms
    fieldsets = (
        ("Login element", {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'profile_img', 'date_of_birth')}),
        # ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Customize the add form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'phone',
                'subscribe_type',
                'profile_img',
                'date_of_birth',
            ),
        }),
    )
    # Customize the search fields
    search_fields = ('email',)
    # Customize the ordering of records
    ordering = ('first_name',)


admin.site.register(CustomUser, CustomUserAdmin)