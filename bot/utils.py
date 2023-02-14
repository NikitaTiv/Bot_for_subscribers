from telegram import ReplyKeyboardMarkup, KeyboardButton

from database.model import User


def main_keyboard(user_id: str) -> ReplyKeyboardMarkup:
    """Выводит клавиатуру для стартового меню."""
    user = User.query.filter(User.tg_id == user_id).first()
    if user:
        if user.status == 'subscribed':
            reply_keyboard = [
                ['Отказаться от подписки 🚫'],
            ]
        if user.status == 'unsubscribed':
            reply_keyboard = [
                ['Подписка на уведомления ✅'],
            ]
    else:
        reply_keyboard = [
            ['Подписка на уведомления ✅'],
        ]

    return ReplyKeyboardMarkup(
                reply_keyboard, resize_keyboard=True,
        )


def subscribe_keyboard() -> ReplyKeyboardMarkup:
    """Функция создает клавиатуру."""
    return ReplyKeyboardMarkup([
        [KeyboardButton('Отправить номер телефона', request_contact=True)], ['Возврат в предыдущее меню ↩️'],
    ], resize_keyboard=True)
