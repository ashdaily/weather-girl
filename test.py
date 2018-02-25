 
import requests
import time
import pytemperature
weather = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=melbourne&APPID=f2f33dbceea19eef373a3972938b7cb1")
api_data = weather.json()
  
temp = []
humidity = []
wind = []
label = []
pressure = []
counter = 0
for  index, item in enumerate(api_data["list"][0:6]):
	print index
	label.append(item["dt_txt"]+" ,"+item["weather"][0]["description"])

	humidity.append(item["main"]["humidity"])
	wind.append(item["wind"]["speed"])
	pressure.append(item["main"]["pressure"])
	temp.append( pytemperature.k2c(item["main"]["temp"]))
	print "****"

print label
print humidity
print wind
print pressure
print temp

	
