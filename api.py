import requests

def forecast(latitude, longtitude):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude)+'&longitude='+str(longtitude)+'&hourly=temperature_2m,apparent_temperature')
    return r.json()
print(forecast(50.4422, 30.5367)['hourly']['temperature_2m'])

def get_forecast(latitude, longtitude, offset):
    """
    Returns string with forecast given to user
    """
    return "18 C, 8м/с"
    
def get_forecast_from_api(latitude, longtitude, offset):
    """ request.get ... """
    return ""

def get_temp_from_json(json_weather):
    return ""

def get_cloud_from_json(json_weather):
    return ""

def get_rain_from_json(json_weather):
    return ""

def get_wind_from_json(json_weather):
    return ""

def get_sunrise_from_json(json_weather):
    return ""
