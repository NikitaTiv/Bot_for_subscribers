import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from bot.handlers import start_menu, user_phone_number, subscribe, unsubscribe
from settings_box.settings import API_KEY

logging.basicConfig(filename='bot.log',
                    format='[%(asctime)s][%(levelname)s] => %(message)s',
                    level=logging.INFO)


def tg_bot() -> None:
    """Run the bot."""
    mybot = Updater(API_KEY, use_context=True)

    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', start_menu))
    dp.add_handler(MessageHandler(Filters.contact, user_phone_number))
    dp.add_handler(MessageHandler(Filters.regex('^(Подписка на уведомления ✅)$'), subscribe))
    dp.add_handler(MessageHandler(Filters.regex('^(Отказаться от подписки 🚫)$'), unsubscribe))
    dp.add_handler(MessageHandler(Filters.regex('^(Возврат в предыдущее меню ↩️)$'), start_menu))

    mybot.start_polling()
    mybot.idle()
