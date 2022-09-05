from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.forms import UserChangeForm, UserCreationForm
from account.models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Customize the behavior of the admin panel with Custom User model."""

    ordering = ("email",)
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ("email", "first_name", "last_name", "is_staff")

    fieldsets = (
        (
            "Personal Info",
            {
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "phone",
                    "portfolio_email",
                    "about",
                    "image",
                    "theme",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("date_joined", "last_login")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    readonly_fields = ["date_joined", "last_login"]


admin.site.register(CustomUser, CustomUserAdmin)
