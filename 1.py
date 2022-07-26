import requests

def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude)+'&longitude='+str(longtitude)+'&hourly=temperature_2m,apparent_temperature')
    return r.json()
print(forecast(50.4422, 30.5367)['hourly']['temperature_2m'])
