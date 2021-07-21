import requests
import os
from datetime import datetime
import time

res = requests.get('https://ipinfo.io/')
data = res.json()
city = data['city']
user_api = 'fdf44e726eb32e35c792708deb85dedf'

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")



location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]

print("Latitude : ", latitude)
print("Longitude : ", longitude)
print("City : ", city)


print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(city.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')





time.sleep('3')
