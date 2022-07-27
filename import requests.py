import requests
from datetime import datetime, timedelta
import telebot

bot = telebot.TeleBot("5434796681:AAE2L-1SX3evqsgGZphxg-UQNCZrmyLombY", parse_mode=None)
def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude)+'&longitude='+str(longtitude)+'&hourly=temperature_2m,apparent_temperature')
    return r.json()

shirota = 48.2085
dolgota = 16.3721

s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
b = forecast(shirota,dolgota)['hourly']['time']
a = forecast(shirota, dolgota)['hourly']['temperature_2m']
a1 = forecast(shirota,dolgota)['hourly']['apparent_temperature']
bl = list(zip(b, a, a1))

@bot.message_handler(commands=['temperature'])
def temperature_weather(message):
    message1 = ''
    for x in bl:
        if x[0] == s:
            message1+=str(f"Температурка:{ round(x[1])}℃ 🌡\n")
            message1+=str(f"По ощущениям:{round(x[2])} ℃ 🌡")
            break

    bot.send_message(message.chat.id, message1)


bot.infinity_polling()