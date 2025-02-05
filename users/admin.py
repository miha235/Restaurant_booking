from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "phone_number",
        "country",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (("Credentials"), {"fields": ("email", "password")}),
        (("Personal info"), {"fields": ("avatar", "phone_number", "country")}),
        (
            ("Permissions"),
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


# @admin.register(User)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'category')
#     list_filter = ('category',)
#     search_fields = ('name', 'description')
