from rest_framework import serializers
from apps.user.models import TelegramUser


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = (
            "telegram_id",
            "username",
            "phone_number",
            "full_name",
        )
