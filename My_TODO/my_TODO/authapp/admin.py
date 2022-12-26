from django.contrib import admin
from authapp import models as mainapp_models


@admin.register(mainapp_models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'user_category',
                    'is_active',
                    'date_joined',
                    ]
