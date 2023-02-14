from telegram import Update

from bot.utils import main_keyboard, subscribe_keyboard
from database.db import db_session
from database.model import User


def start_menu(update: Update, context) -> None:
    """Выводит для пользователя стартовое меню."""
    update.message.reply_text(
        'Pass',
        reply_markup=main_keyboard(update.message.chat.id),
    )


def subscribe(update: Update, context) -> None:
    """Предлагает пользователю подписаться на уведомления."""
    update.message.reply_text(
        'Для подписки на уведомления необходимо прислать номер телефона.',
        reply_markup=subscribe_keyboard(),
    )


def unsubscribe(update: Update, context) -> None:
    """Меняет статус пользователя на 'unsubscribed'."""
    user = User.query.filter(User.tg_id == update.message.chat.id).first()
    user.status = 'unsubscribed'
    db_session.commit()

    update.message.reply_text(
        'Ваша подписка отменена',
        reply_markup=main_keyboard(update.message.chat.id),
    )


def user_phone_number(update: Update, context) -> None:
    """Запрашивает у пользователя номер телефона, меняет его статус на 'subscribed'."""
    user = User.query.filter(User.tg_id == update.message.contact.user_id).first()
    if user:
        user.status = 'subscribed'
        db_session.commit()
    else:
        if len(update.message.contact.phone_number) == 11:
            update.message.contact.phone_number = '+7' + update.message.contact.phone_number[1:]
        user = [
                {'first_name': update.message.contact.first_name, 'second_name': update.message.contact.last_name,
                'nickname': update.message.chat.username, 'tg_id': update.message.contact.user_id,
                'phone_number': update.message.contact.phone_number, 'status': 'subscribed', }
        ]
        db_session.bulk_insert_mappings(User, user)
        db_session.commit()

    update.message.reply_text(
        'Спасибо за подписку 👍',
        reply_markup=main_keyboard(update.message.chat.id),
    )
