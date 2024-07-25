from apps.common.models import BaseModel
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TelegramUser(BaseModel):
    username_validator = UnicodeUsernameValidator()

    phone_number = models.CharField(max_length=20, null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    telegram_id = models.CharField(
        max_length=50, null=True,
        db_index=True, unique=True,
        help_text="Telegram id of the user",
        error_messages={
            "unique": "This telegram id is already registered."
        }
    )

    def __str__(self):
        return self.username

    @property
    def tg_link(self):
        if self.phone_number:
            return f"https://t.me/{self.phone_number}"
        if self.username:
            return f"https://t.me/{self.username}"
        return None
