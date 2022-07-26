import requests
from datetime import datetime

def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude='+str(latitude)+'&longitude='+str(longtitude)+'&hourly=cloudcover')
    return r.json()
s = datetime.now().replace(minute=0).isoformat(timespec="minutes")
x = 0
a = forecast(50.4422, 30.5367)['hourly']['time']
b = forecast(50.4422, 30.5367)['hourly']['cloudcover']
ab = list(zip(a,b))
for x in ab:
    if x[0] == s:
        print("текущая облачность : ", x[1])
        break
