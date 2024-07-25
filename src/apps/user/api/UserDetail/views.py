from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.user.models import TelegramUser

from .serializer import UserRetrieveSerializer


class UserRetrieveView(RetrieveAPIView):
    serializer_class = UserRetrieveSerializer
    queryset = TelegramUser.objects.all()
    permission_classes = [AllowAny]
    lookup_field = "telegram_id"


