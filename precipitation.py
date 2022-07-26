import requests
from datetime import datetime 
def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude)+'&longitude='+str(longtitude)+'&hourly=rain,showers,snowfall')
    return r.json()
s= datetime.now().replace(minute=0).isoformat(timespec="minutes")
x = 0
b = forecast(50.4422, 30.5367)['hourly']['time']
a = forecast(50.4422, 30.5367)['hourly']['snowfall']
a1 = forecast(50.4422, 30.5367)['hourly']['rain']
a2 = forecast(50.4422, 30.5367)['hourly']['showers']
b1= list(zip(b, a, a1, a2))
for x in b1:
    if x[0] == s:
        print("снег: ", x[1])
        print("дождь: ", x[2])
        print("душ: ", x[3])
        break