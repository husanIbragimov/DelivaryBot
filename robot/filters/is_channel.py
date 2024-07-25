from aiogram.types import Message
from aiogram.filters import BaseFilter


class IsChannel(BaseFilter):
    async def __call__(self, message: Message):
        return message.chat.type == 'channel' 