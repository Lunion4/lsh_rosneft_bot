import requests
from datetime import datetime

def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude)+'&longitude='+str(longtitude)+'&hourly=temperature_2m,apparent_temperature,rain,snowfall,relativehumidity_2m,windspeed_10m,windgusts_10m,weathercode&daily=sunrise,sunset,weathercode&timezone=UTC')
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
w_code = forecast(50.4422, 30.5367)['hourly']['weathercode']
s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
s1= datetime.date
b = forecast(50.4422, 30.5367)['hourly']['time']
a = forecast(50.4422, 30.5367)['hourly']['temperature_2m']
a1 = forecast(50.4422, 30.5367)['hourly']['apparent_temperature']
a2 = forecast(50.4422, 30.5367)['hourly']['rain']
a3 = forecast(50.4422, 30.5367)['hourly']['snowfall']
a4 = forecast(50.4422, 30.5367)['hourly']['relativehumidity_2m']
a5 = forecast(50.4422, 30.5367)['hourly']['windspeed_10m']
a6 = forecast(50.4422, 30.5367)['hourly']['windgusts_10m']
bl = list(zip(b, a, a1, a2, a3, a4, a5, a6))
for x in bl:
    if x[0] == s:
        print("Температурка: ", round(x[1]), "℃ 🌡")
        print("По ощущениям: ", round(x[2]), "℃ 🌡")
        print("Дождик: ", x[3], "🌧")
        print("Снежок: ", x[4], "❄️")
        print("Влажненько: ", round(x[5]), "% 💧")
        print("Ветерок: ", x[6], "м\с 🌬")
        print("Злой ветерок: ", x[7], "м\с 🌪")
        break
sunrise = forecast(50.4422, 30.5367)['daily']['sunrise']
sunset = forecast(50.4422, 30.5367)['daily']['sunset']
print("Солнышко просыпается в",datetime.fromisoformat(sunrise[0]).time().isoformat(timespec="minutes"), "🌝")
print("Солнышко засыпает в",datetime.fromisoformat(sunset[0]).time().isoformat(timespec="minutes"), "🌚")
print("В общем ", weather(w_code))