import requests
from datetime import datetime, timedelta
import telebot
import random


bot = telebot.TeleBot("5434796681:AAE2L-1SX3evqsgGZphxg-UQNCZrmyLombY", parse_mode=None)

def rand_img():
    file = 'gifs.txt'
    myfile = open(file, mode='r', encoding='utf_8')
    if file:
        spisok = myfile.readlines()
    index = random.randint(0, len(spisok)-1)
    return spisok[index]

def rand_meme():
    file = 'gifs_meme.txt'
    myfile = open(file, mode='r', encoding='utf_8')
    if file:
        spisok = myfile.readlines()
    index = random.randint(0, len(spisok)-1)
    return spisok[index]

def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude)+'&longitude='+str(longtitude)+'&hourly=temperature_2m,apparent_temperature,rain,snowfall,relativehumidity_2m,windspeed_10m,windgusts_10m,weathercode,cloudcover_low,surface_pressure&daily=sunrise,sunset,weathercode&timezone=UTC')
    return r.json()
def weather(w_code):
    if w_code == 0 or 1:
        return 'ясненько'
    elif w_code == 2 or 3:
        return 'пасмурненько'
    elif w_code == 45 or 48:
        return 'туманно'
    elif w_code == 51 or 53 or 56 or 61 or 66:
        return 'добрый дождик'
    elif w_code == 55 or 57 or 63 or 65 or 67 or 80 or 81 or 82:
        return 'злой дождик'
    elif w_code == 71 or 73 or 75 or 77 or 85 or 86:
        return 'снегопад'
    elif w_code == 95 or 96 or 99:
        return 'гроза'
def is_rainy(times, rainy, code):
    s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
    s1 = datetime.now()+ timedelta(hours=12)
    all = list(zip(times, rainy, code))
    time_now = int(datetime.utcnow().strftime('%H'))
    time_to = int(s1.strftime('%H'))
    rain_start = 0
    for i in range(time_now, time_to):
        if all[i][1] > 0 and (all[i][2] == 61 or all[i][2] == 63 or all[i][2] == 65 or all[i][2] == 66 or all[i][2] == 67 or all[i][2] == 80 or all[i][2] == 81 or all[i][2] == 82 or all[i][2] == 95 or all[i][2] == 96 or all[i][2] == 99):
            rain_start = all[i][0]
            break
    if rain_start == 0:
        return "В ближайшее время дождик не планируется"
    else:
        rain_start = datetime.fromisoformat(rain_start)
        return "Возьмите зонтики, дождик начнется в "+ str(rain_start.strftime('%H'))+" с чем-то:)"


def spiski(shirota, dolgota):    
    fc = forecast(shirota, dolgota)['hourly']
    w_code = fc['weathercode']
    b = fc['time']
    a = fc['temperature_2m']
    a1 = fc['apparent_temperature']
    a2 = fc['rain']
    a3 = fc['snowfall']
    a4 = fc['relativehumidity_2m']
    a5 = fc['windspeed_10m']
    a6 = fc['windgusts_10m']
    a7 = fc['cloudcover_low']
    a8 = fc['surface_pressure']
    bl = list(zip(b, a, a1, a2, a3, a4, a5, a6, a7, a8))
    return bl, w_code

def all_weather(shirota, dolgota):
    s = datetime.utcnow().replace(minute=0).isoformat(timespec="minutes")
    bl, w_code = spiski(shirota, dolgota)
    message1 = ''
    for x in bl:
        if x[0] == s:
            message1 += str(f"Температурка: {round(x[1])}℃ 🌡 \n")
            message1 += str(f"По ощущениям: {round(x[2])} ℃ 🌡 \n")
            message1 += str(f"Дождик: {x[3]} мм 🌧\n")
            message1 += str(f"Снежок: {x[4]} мм ❄️\n")
            message1 += str(f"Влажненько: {round(x[5])} % 💧\n")
            message1 += str(f"Ветерок: {x[6]} м\с 🪁\n")
            message1 += str(f"Злой ветерок: {x[7]} м\с 🌪\n")
            message1 += str(f"Тучки: {round(x[8])} % ☁️\n")
            message1 += str(f"Давление: {int(x[9]) *0.75} мм рт.ст. 👵 \n")
            break
    sunrise = forecast(shirota, dolgota)['daily']['sunrise']
    sunset = forecast(shirota, dolgota)['daily']['sunset']
    message1 += str(f'Солнышко просыпается в {(datetime.fromisoformat(sunrise[0])+timedelta(hours=3)).time().isoformat(timespec="minutes")} 🌝 (по МСК)\n')
    message1 += str(f'Солнышко засыпает в {(datetime.fromisoformat(sunset[0])+timedelta(hours=3)).time().isoformat(timespec="minutes")} 🌚 (по МСК)\n')
    message1 += str(f'В общем {weather(w_code)} \n') 
    #message1 += str(is_rainy(s, b, a2, w_code))
    return message1

def wind(shirota, dolgota):
    s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
    bl, w_code= spiski(shirota, dolgota)
    for x in bl:
        if x[0] == s:
            return f"Ветерок: {x[6]} м\с 🪁\nЗлой ветерок: {x[7]} м\с 🌪"
def pressure(shirota, dolgota):
    s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
    bl, w_code= spiski(shirota, dolgota)
    message1=''
    for x in bl:
        if x[0] == s:
            message1 += str(f"Давление: {int(x[9])*0.75} мм рт.ст. 👵 \n") 
            break
    return message1         


def rainy_weather(shirota, dolgota):
    s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
    bl, w_code = spiski(shirota, dolgota)
    message1 = ''
    for x in bl:
        if x[0] == s:
            message1 += str(f"Дождик: {x[3]}мм 🌧\n")
            message1 += str(f"Снежок: {x[4]}мм ☃️\n")
            
            break
    message1 += str(is_rainy([x[0] for x in bl], [x[3] for x in bl], w_code))
    return message1


def cloudcover(shirota, dolgota):
    s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
    bl, w_code = spiski(shirota, dolgota)
    message1 = ''
    for x in bl:
        if  x[0] == s:
            message1 +=str(f"Тучки {round(x[8])}%☁")
            break
    return message1

def temperature_weather(shirota, dolgota):
    s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
    bl, w_code = spiski(shirota, dolgota)
    message1 = ''
    for x in bl:
        if x[0] == s:
            message1+=str(f"Температурка: { round(x[1])}℃ 🌡\n")
            message1+=str(f"По ощущениям: {round(x[2])} ℃ 🌡")
            break

    return message1

