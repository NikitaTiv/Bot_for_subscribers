import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from database.model import User
from settings_box.settings import API_KEY


def inline_button() -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру."""
    reply_keyboard = [
        [InlineKeyboardButton('Вперед к новым платежам 🚀', url='http://127.0.0.1:5000')],
    ]

    return InlineKeyboardMarkup(reply_keyboard, resize_keyboard=True,)

def send_message(text: str, id: int) -> None:
    """Отправляет пользователю сообщение в бот."""
    token = API_KEY
    keyboard = '{"inline_keyboard": [[{"text": "Привет!", "url": "https://sky.pro/"}]]}' #callback_data
    chat_id = str(id)
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text + "&reply_markup=" + keyboard
    results = requests.post(url_req)


def send_photo(img_url:str, text: str, id: int) -> None:
    """Отправляет пользователю картинку + сообщение в бот."""
    files = {'photo': open(img_url, 'rb')}
    token = API_KEY
    chat_id = str(id)
    url_req = "https://api.telegram.org/bot" + token + "/sendPhoto" + "?chat_id=" + chat_id + "&caption=" + text
    results = requests.post(url_req, files=files)


if __name__ == '__main__':
    text = input('Что вы хотите отправить? (Текст / Фото): ')
    list_user = User.query.filter(User.status=='subscribed').all()
    if text.lower() == 'текст':
        message = input('Введите текст для отправки: ')
        for user in list_user:
            send_message(message, user.tg_id)
    if text.lower() == 'фото':
        img_url = input('Укажите путь к фотографии: ')
        text = input('Введите текст для отправки: ')
        for user in list_user:
            send_photo(img_url, text, user.tg_id)
            


        