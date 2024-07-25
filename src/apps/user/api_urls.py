from django.urls import path

from .api import UserCreateView, UserRetrieveView

app_name = 'user'

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('me/<str:telegram_id>/', UserRetrieveView.as_view(), name='retrieve_user'),
]
