from django.contrib import admin

from .models import TelegramUser

admin.site.register(TelegramUser)   # Register the TelegramUser model in the admin panel
