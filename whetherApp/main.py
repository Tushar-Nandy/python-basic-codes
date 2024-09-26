import requests
import smtplib

API_KEY="f7eee4c919ac4c9361ebed710b3badfa"
LAT =19.418343
LON = 72.795593
API_END =f"https://api.openweathermap.org/data/2.5/forecast"
wheather_params={
    'lat':LAT,
    'lon':LON,
    'cnt':4,
    'appid':API_KEY
}
will_rain =False

res=requests.get(API_END,params=wheather_params)
data = res.json()
for i in range(4):
    whether_list = data['list'][1]
    weather = whether_list['weather']
    for j in range(len(weather)):
        weather_data = weather[j]
        weather_id = weather_data['id']
        if weather_id <700:
            will_rain =True
if will_rain:
    print("Will Rain")