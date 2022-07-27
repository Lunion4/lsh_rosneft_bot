import requests
from datetime import datetime
import telebot

bot = telebot.TeleBot("5470137243:AAH8xEBtQeVFzn3zhAX9Ews8FDMt3AXO3yA", parse_mode=None)

shirota = 48.2085
dolgota = 16.3721

def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude)+'&longitude='+str(longtitude)+'&hourly=rain,snowfall')
    return r.json()

s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
a2 = forecast(shirota, dolgota)['hourly']['rain']
a3 = forecast(shirota, dolgota)['hourly']['snowfall']
time = forecast(shirota,dolgota)['hourly']['time']
d1 = list(zip(time,a2, a3))


@bot.message_handler(commands=['rain'])
def rainy_weather(message):
    message1 = ''
    for x in d1:
        if x[0] == s:
            message1 += str(f"Дождик: {x[1]}🌧")
            message1 += str(f"Снежок: {x[2]}☃️")
            break
    bot.send_message(message.chat.id, message1)
bot.infinity_polling()