import requests
from datetime import datetime

def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude='+str(latitude)+'&longitude='+str(latitude)+'&hourly=windspeed_10m,windspeed_80m,windspeed_120m,windspeed_180m,windgusts_10m')
    return r.json()
s = datetime.now().replace(minute=0).isoformat(timespec='minutes')
x = 0 
b = forecast(50.4422, 30.5367)['hourly']['time']
a1 = forecast(50.4422, 30.5367)['hourly']['windspeed_10m']
a2 = forecast(50.4422, 30.5367)['hourly']['windspeed_80m']
a3 = forecast(50.4422, 30.5367)['hourly']['windspeed_120m']
a4 = forecast(50.4422, 30.5367)['hourly']['windspeed_180m']
a5 = forecast(50.4422, 30.5367)['hourly']['windgusts_10m']
bl = list(zip(b, a1, a2, a3, a4, a5))
for x in bl:
    if x[0]==s:
        print ('Текущая скорость вестра на высоте 10м:', x[1])
        print ('Текущая скорость ветра на высоте 80м:', x[2])
        print ('Текущая скорость ветра на высоте 120м:', x[3])
        print ('Текущая скорость ветра на высоте 180м:', x[4])
        print ('Текущие порывы ветра на высоте 10м:', x[5])
        break


