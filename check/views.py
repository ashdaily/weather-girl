from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.gis.geoip2 import GeoIP2
import requests
import time
import pytemperature

# Create your views here.

def index(request):
    # g = GeoIP2()
    # # ip = request.META.get("REMOTE_ADDR", None)
    # ip = "72.229.28.185"
    # print ip
    # if ip:
    #     city = g.city(ip)["city"]
    # else:
    #     city = "Tokyo"
    # print city
    #
    #

    # print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["sys"]["sunset"]))
     
 

    return render(request,"check/index.html")



 


def weather_today(request):
    g = GeoIP2()
    # ip = request.META.get("REMOTE_ADDR", None)
    ip = "72.229.28.185"
    print ip
    if ip:
        city = g.city(ip)["city"]
    else:
        city = "Tokyo"
    print city
    weather_forecast = requests.get(
        "http://api.openweathermap.org/data/2.5/forecast?q="+"bangalore"+"&APPID=f2f33dbceea19eef373a3972938b7cb1")
    data_weather_forecast = weather_forecast.json()
     

    temp = []
    humidity = []
    wind = []
    label = []
    pressure = []
    for item in data_weather_forecast["list"][0:5]:
        label.append(item["dt_txt"][11:13]+ " ," + item["weather"][0]["description"])
        
        humidity.append(item["main"]["humidity"])
        wind.append(item["wind"]["speed"])
        pressure.append(item["main"]["pressure"])
        temp.append(item["main"]["temp"]-273.15)
    print label
    print temp
    
    return JsonResponse({'status': 'True','label':label,'temp':temp,"wind":wind,"pressure":pressure,"humidity":humidity})