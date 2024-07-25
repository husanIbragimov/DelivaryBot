from django.db import models

from apps.common.models import BaseModel


class Service(BaseModel):
    user = models.ForeignKey('user.TelegramUser', on_delete=models.CASCADE, related_name='services', related_query_name='service')
    phone_number = models.CharField(max_length=20)
    deliverer = models.ForeignKey('user.TelegramUser', on_delete=models.CASCADE, related_name='deliverer_services', related_query_name='deliverer_service')
    notes = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number
    
    @property
    def tg_link(self):
        if self.phone_number:
            return f"https://t.me/{self.phone_number}"
        return None
