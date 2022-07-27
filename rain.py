import requests
from datetime import datetime, timedelta

def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude)+'&longitude='+str(longtitude)+'&hourly=rain,weathercode')
    return r.json()


s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
s1 = datetime.now()+ timedelta(hours=12)
times=forecast(48.2085, 16.3721)['hourly']['time']
rainy = forecast(48.2085, 16.3721)['hourly']['rain']
code = forecast(48.2085, 16.3721)['hourly']['weathercode']
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

