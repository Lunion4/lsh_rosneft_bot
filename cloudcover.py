import requests
import telebot
from datetime import datetime

bot = telebot.TeleBot ("5420997686:AAG6yf80LRLv3FjS8SbvDB_RfNg5BCiipjM")
def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude='+str(latitude)+'&longitude='+str(longtitude)+'&hourly=cloudcover')
    return r.json()

shirota = 48.2085
dolgota = 16.3721

s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
a7 = forecast(shirota,dolgota)['hourly']['cloudcover']
time = forecast(shirota,dolgota)['hourly']['time']
dl = list(zip(time,a7))

@bot.message_handler(commands=['cloud'])
def cloudcover(message):
    message1 = ''
    for x in dl:
        if  x[0] == s:
            message1 +=str(f"Тучки {x[1]}☁")
            break
    bot.send_message(message.chat.id, message1)

bot.infinity_polling()