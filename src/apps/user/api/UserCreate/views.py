from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from apps.user.models import TelegramUser

from .serializer import UserCreateSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = TelegramUser.objects.all()
    permission_classes = [AllowAny]

