from django.contrib.auth import admin

from django.contrib.admin import register
from authapp import models as mainapp_models


@register(mainapp_models.CustomUser)
class CustomUserAdmin(admin.UserAdmin):
    readonly_fields = ['date_joined', 'last_login']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", 'email', 'user_category'),
            },
        ),
    )
    list_display = ('username',
                    'email',
                    'user_category',
                    'is_active',
                    'date_joined',
                    'password'
                    )
