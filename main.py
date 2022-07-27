import requests
from datetime import datetime, timedelta
import telebot


bot = telebot.TeleBot("5434796681:AAE2L-1SX3evqsgGZphxg-UQNCZrmyLombY", parse_mode=None)

def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude)+'&longitude='+str(longtitude)+'&hourly=temperature_2m,apparent_temperature,rain,snowfall,relativehumidity_2m,windspeed_10m,windgusts_10m,weathercode,cloudcover&daily=sunrise,sunset,weathercode&timezone=UTC')
    return r.json()
def weather(w_code):
    if w_code == 0 or 1 or 2:
        return 'ясненько'
    elif w_code == 3 or 45 or 48:
        return 'пасмурненько'
    elif w_code == 51 or 53 or 56 or 61 or 66:
        return 'добрый дождик'
    elif w_code == 55 or 57 or 63 or 65 or 67 or 80 or 81 or 82:
        return 'злой дождик'
    elif w_code == 71 or 73 or 75 or 77 or 85 or 86:
        return 'снегопад'
    elif w_code == 95 or 96 or 99:
        return 'гроза'
def is_rainy(s, times, rainy, code):
    s1 = datetime.now()+ timedelta(hours=12)
    all = list(zip(times, rainy, code))
    time_now = int(datetime.today().strftime('%H'))
    time_to = int(s1.strftime('%H'))
    rain_start = 0
    for i in range(time_now, time_to):
        if all[i][1] > 0 and (all[i][2] == 61 or all[i][2] == 63 or all[i][2] == 65 or all[i][2] == 66 or all[i][2] == 67 or all[i][2] == 80 or all[i][2] == 81 or all[i][2] == 82 or all[i][2] == 95 or all[i][2] == 96 or all[i][2] == 99):
            rain_start = all[i][0]
            break
    if rain_start == 0:
        print("в ближайшее время дождик не планируется")
    else:
        rain_start = datetime.fromisoformat(rain_start)
        print("Возьмите зонтики, дождик начнется в", rain_start.strftime('%H'), "с чем-то:)")



shirota = 48.2085
dolgota = 16.3721

w_code = forecast(shirota, dolgota)['hourly']['weathercode']
s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
b = forecast(shirota, dolgota)['hourly']['time']
a = forecast(shirota, dolgota)['hourly']['temperature_2m']
a1 = forecast(shirota, dolgota)['hourly']['apparent_temperature']
a2 = forecast(shirota, dolgota)['hourly']['rain']
a3 = forecast(shirota, dolgota)['hourly']['snowfall']
a4 = forecast(shirota, dolgota)['hourly']['relativehumidity_2m']
a5 = forecast(shirota, dolgota)['hourly']['windspeed_10m']
a6 = forecast(shirota, dolgota)['hourly']['windgusts_10m']
a7 = forecast(shirota, dolgota)['hourly']['cloudcover']
bl = list(zip(b, a, a1, a2, a3, a4, a5, a6, a7))

@bot.message_handler(commands=['all'])
def all_weather(message):
    message1 = ''
    for x in bl:
        if x[0] == s:
            message1 += str(f"Температурка: {round(x[1])}℃ 🌡")
            message1 += str(f"По ощущениям: {round(x[2])} ℃ 🌡")
            message1 += str(f"Дождик: {x[3]} 🌧")
            message1 += str(f"Снежок: {x[4]} ❄️")
            message1 += str(f"Влажненько: {round(x[5])} % 💧")
            message1 += str(f"Ветерок: {x[6]} м\с 🌬")
            message1 += str(f"Злой ветерок: {x[7]} м\с 🌪")
            message1 += str(f"Тучки {x[8]} ☁️")
            break
    sunrise = forecast(shirota, dolgota)['daily']['sunrise']
    sunset = forecast(shirota, dolgota)['daily']['sunset']
    message1 += str(f'Солнышко просыпается в {datetime.fromisoformat(sunrise[0]).time().isoformat(timespec="minutes")} 🌝')
    message1 += str(f'Солнышко засыпает в {datetime.fromisoformat(sunset[0]).time().isoformat(timespec="minutes")} 🌚')
    message1 += str(f'В общем {weather(w_code)}') 
    message1 += str(is_rainy(s, b, a2, w_code))
    bot.send_message(message.chat.id, message1)


bot.infinity_polling()
