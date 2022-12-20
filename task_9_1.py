''' Задача 9_1. Написать простой парсер для извлечения информации с любого сайта.'''

import requests
import json
import datetime as dt

#   Какой сюртук и какие шузы надеть сегодня? Узнаем погоду за окном. Важно! VPN и прочие паранойи типа Tor делают прогноз погоды "удивительным"
today = dt.datetime.utcnow() + dt.timedelta(hours=3)
print(f"Сейчас у Вас {today.strftime('%d %B %Y %X')}")
URL = 'http://wttr.in'
weather_params = {
    '0': '',
    'T': '',
    'lang': 'ru'
}
response = requests.get(URL, params=weather_params)
print(response.text)

#   Посмотрим, почём сегодня царские казначеи оценивают заморские дукаты и манаты
URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(URL)
# print(response.text)   - собственно, курс всех валют
dict_json = json.loads(response.text)
usd_course = f"Курс USD, установленный ЦБР на {today.strftime('%d %B %Y')} равен {dict_json['Valute']['USD']['Value']} руб."
eur_course = f"Курс Euro, установленный ЦБР на {today.strftime('%d %B %Y')} равен {dict_json['Valute']['EUR']['Value']} руб."
print(usd_course)
print(eur_course)