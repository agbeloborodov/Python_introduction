from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from credits_bot import bot_token
import requests
import json
import datetime as dt
from bs4 import BeautifulSoup as bs


''' /start      - приветствие жизнерадостного бота
    /nigga      - отношение жизнерадостного бота к окружающей суете
    /get_menu   - вызов меню
    any_text    - ответ на любой вопрос                     '''

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

def start (update, context):                # приветствие жизнерадостного бота
    context.bot.send_message(update.effective_chat.id, "Й-е-е, нигга. Джа!")

def message(update, context):               # отношение жизнерадостного бота к окружающей суете
    if update.message.text == '/nigga':
        context.bot.send_message(update.effective_chat.id, "Я плохой старый нигга. Миссисипи, плот, белый масса Гек, растафара, ДЖА!")
    else:
        context.bot.send_message(update.effective_chat.id, "Моя глупый старый нигга. Моя твоя мало-мало не понимай. Но будь уверен: True == 42.")

def weather_today():                        # погода за своим окном online
    URL = 'http://wttr.in'
    weather_params = {
        '0': '',
        'T': '',
        'lang': 'ru'}
    response = requests.get(URL, params=weather_params)
    return response.text

def weather_irkutsk():                      # погода в Иркутске
    API_key = '4321a3d417b53045aa1b6617c529c910'
    city_name = 'Irkutsk'
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=ru")
    dict_js = json.loads(response.text)
    weather_irkutsk = (f"Погода в {city_name} на сегодня: ветер {dict_js['wind']['speed']} м/с, температура {dict_js['main']['temp']} С ")
    return weather_irkutsk

def money_course():                         # курс валют на текущую дату, установленный ЦБ
    today = dt.datetime.utcnow() + dt.timedelta(hours=3)
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(URL)
    dict_json = json.loads(response.text)
    usd_course = f"Курс USD, установленный ЦБР на {today.strftime('%d %B %Y')} равен {dict_json['Valute']['USD']['Value']} руб."
    eur_course = f"Курс Euro, установленный ЦБР на {today.strftime('%d %B %Y')} равен {dict_json['Valute']['EUR']['Value']} руб."
    return(f"{usd_course}\n{eur_course}")

def sport_today():                          # первые пять новостей спорта на портале mail.ru
    temp_text = requests.get("https://sportmail.ru/").text
    soup = bs(temp_text, 'html.parser')
    result = soup.find_all('li', class_ = 'list__item')
    sport_news = ''
    for item in range(5):
        sport_news = sport_news + f"{result[item].text}\n"
    return sport_news


def get_menu(update, context):              # формирование меню
    keyboard = [
        [InlineKeyboardButton("Текущее время", callback_data = '1')],
        [InlineKeyboardButton("Текущий курс валют", callback_data = '2')],
        [InlineKeyboardButton("Погода в Иркутске", callback_data = '3')],
        [InlineKeyboardButton("Погода за окном", callback_data = '4')],
        [InlineKeyboardButton("Новости спорта", callback_data = '5')],
        [InlineKeyboardButton("Мудрость Цзы", callback_data = '6')]
    ]
    update.message.reply_text('Нажми на кнопку - получишь результат ', reply_markup=InlineKeyboardMarkup(keyboard))

def button(update, context):                # реакция бота на нажатый юзверем батон
    query = update.callback_query
    query.answer()
    if query.data == '1':
        context.bot.send_message(update.effective_chat.id, f"Сейчас у Вас {(dt.datetime.utcnow() + dt.timedelta(hours=3)).strftime('%d %B %Y %X')}")
    elif query.data == '2':
        context.bot.send_message(update.effective_chat.id, f"{money_course()}")
    elif query.data == '3':
        context.bot.send_message(update.effective_chat.id, f"{weather_irkutsk()}")
    elif query.data == '4':
        context.bot.send_message(update.effective_chat.id, f"{weather_today()}")
    elif query.data == '5':
        context.bot.send_message(update.effective_chat.id, f"{sport_today()}")
    elif query.data == '6':
        context.bot.send_message(update.effective_chat.id, "Не пытайся согнуть ложку. Это невозможно. Для начала нужно понять главное - ЛОЖКИ НЕТ. Это не ложка гнётся, всё дело в тебе.")

start_handler = CommandHandler('start', start)
getmenu_handler = CommandHandler('get_menu', get_menu)
message_handler = MessageHandler(Filters.text, message)
button_handler = CallbackQueryHandler(button)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(getmenu_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(button_handler)

updater.start_polling()
updater.idle()