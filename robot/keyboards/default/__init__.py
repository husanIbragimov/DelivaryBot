from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛒 Online Shopping"),
        ],
        [
            KeyboardButton(text="💡 Service hizmatlar"),
        ]

    ],
    resize_keyboard=True, input_field_placeholder="Menu"
)