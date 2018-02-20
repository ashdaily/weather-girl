from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
import requests
import time

# Create your views here.

def index(request):
    g = GeoIP2()
    # ip = request.META.get("REMOTE_ADDR", None)
    ip = "72.229.28.185"
    print ip
    if ip:
        city = g.city(ip)["city"]
    else:
        city = "Tokyo"
    print city

    report = {
    "cod": "200",
    "message": 0.0049,
    "cnt": 40,
    "list": [
        {
            "dt": 1519128000,
            "main": {
                "temp": 277.18,
                "temp_min": 277.18,
                "temp_max": 279.171,
                "pressure": 1024.3,
                "sea_level": 1028.4,
                "grnd_level": 1024.3,
                "humidity": 92,
                "temp_kf": -1.99
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 2.88,
                "deg": 131.505
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-20 12:00:00"
        },
        {
            "dt": 1519138800,
            "main": {
                "temp": 276.02,
                "temp_min": 276.02,
                "temp_max": 277.508,
                "pressure": 1023.59,
                "sea_level": 1027.49,
                "grnd_level": 1023.59,
                "humidity": 100,
                "temp_kf": -1.49
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n"
                }
            ],
            "clouds": {
                "all": 20
            },
            "wind": {
                "speed": 2.11,
                "deg": 42.5018
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-20 15:00:00"
        },
        {
            "dt": 1519149600,
            "main": {
                "temp": 277.01,
                "temp_min": 277.01,
                "temp_max": 278.005,
                "pressure": 1023.38,
                "sea_level": 1027.27,
                "grnd_level": 1023.38,
                "humidity": 96,
                "temp_kf": -0.99
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n"
                }
            ],
            "clouds": {
                "all": 24
            },
            "wind": {
                "speed": 5.2,
                "deg": 354.508
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-20 18:00:00"
        },
        {
            "dt": 1519160400,
            "main": {
                "temp": 277.62,
                "temp_min": 277.62,
                "temp_max": 278.116,
                "pressure": 1024.68,
                "sea_level": 1028.62,
                "grnd_level": 1024.68,
                "humidity": 90,
                "temp_kf": -0.5
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 56
            },
            "wind": {
                "speed": 4.38,
                "deg": 11.5005
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-20 21:00:00"
        },
        {
            "dt": 1519171200,
            "main": {
                "temp": 279.773,
                "temp_min": 279.773,
                "temp_max": 279.773,
                "pressure": 1025.83,
                "sea_level": 1029.57,
                "grnd_level": 1025.83,
                "humidity": 80,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 80
            },
            "wind": {
                "speed": 3.63,
                "deg": 22.0003
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-21 00:00:00"
        },
        {
            "dt": 1519182000,
            "main": {
                "temp": 280.783,
                "temp_min": 280.783,
                "temp_max": 280.783,
                "pressure": 1024.93,
                "sea_level": 1028.79,
                "grnd_level": 1024.93,
                "humidity": 73,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 88
            },
            "wind": {
                "speed": 2.74,
                "deg": 13.5023
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-21 03:00:00"
        },
        {
            "dt": 1519192800,
            "main": {
                "temp": 281.301,
                "temp_min": 281.301,
                "temp_max": 281.301,
                "pressure": 1024.18,
                "sea_level": 1028.02,
                "grnd_level": 1024.18,
                "humidity": 72,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "clouds": {
                "all": 64
            },
            "wind": {
                "speed": 1.61,
                "deg": 28.0001
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-21 06:00:00"
        },
        {
            "dt": 1519203600,
            "main": {
                "temp": 278.997,
                "temp_min": 278.997,
                "temp_max": 278.997,
                "pressure": 1024.51,
                "sea_level": 1028.49,
                "grnd_level": 1024.51,
                "humidity": 81,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 1.18,
                "deg": 34.0033
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-21 09:00:00"
        },
        {
            "dt": 1519214400,
            "main": {
                "temp": 277.041,
                "temp_min": 277.041,
                "temp_max": 277.041,
                "pressure": 1025.68,
                "sea_level": 1029.65,
                "grnd_level": 1025.68,
                "humidity": 91,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                }
            ],
            "clouds": {
                "all": 44
            },
            "wind": {
                "speed": 1.87,
                "deg": 64.5015
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-21 12:00:00"
        },
        {
            "dt": 1519225200,
            "main": {
                "temp": 278.119,
                "temp_min": 278.119,
                "temp_max": 278.119,
                "pressure": 1026.47,
                "sea_level": 1030.45,
                "grnd_level": 1026.47,
                "humidity": 90,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 2.67,
                "deg": 52.5038
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-21 15:00:00"
        },
        {
            "dt": 1519236000,
            "main": {
                "temp": 278.076,
                "temp_min": 278.076,
                "temp_max": 278.076,
                "pressure": 1027.17,
                "sea_level": 1031.08,
                "grnd_level": 1027.17,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 3.76,
                "deg": 6.00269
            },
            "rain": {
                "3h": 0.24
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-21 18:00:00"
        },
        {
            "dt": 1519246800,
            "main": {
                "temp": 276.119,
                "temp_min": 276.119,
                "temp_max": 276.119,
                "pressure": 1028.86,
                "sea_level": 1032.8,
                "grnd_level": 1028.86,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 88
            },
            "wind": {
                "speed": 4.81,
                "deg": 356.501
            },
            "rain": {
                "3h": 1.335
            },
            "snow": {
                "3h": 0.0975
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-21 21:00:00"
        },
        {
            "dt": 1519257600,
            "main": {
                "temp": 275.987,
                "temp_min": 275.987,
                "temp_max": 275.987,
                "pressure": 1030.89,
                "sea_level": 1034.77,
                "grnd_level": 1030.89,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 4.71,
                "deg": 8.00653
            },
            "rain": {
                "3h": 0.435
            },
            "snow": {
                "3h": 0.0675
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-22 00:00:00"
        },
        {
            "dt": 1519268400,
            "main": {
                "temp": 276.743,
                "temp_min": 276.743,
                "temp_max": 276.743,
                "pressure": 1030.72,
                "sea_level": 1034.55,
                "grnd_level": 1030.72,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 4.41,
                "deg": 19.5009
            },
            "rain": {
                "3h": 0.085
            },
            "snow": {
                "3h": 0.06
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-22 03:00:00"
        },
        {
            "dt": 1519279200,
            "main": {
                "temp": 277.458,
                "temp_min": 277.458,
                "temp_max": 277.458,
                "pressure": 1029.97,
                "sea_level": 1033.96,
                "grnd_level": 1029.97,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 88
            },
            "wind": {
                "speed": 3.97,
                "deg": 26.5
            },
            "rain": {
                "3h": 0.055
            },
            "snow": {},
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-22 06:00:00"
        },
        {
            "dt": 1519290000,
            "main": {
                "temp": 276.916,
                "temp_min": 276.916,
                "temp_max": 276.916,
                "pressure": 1030.97,
                "sea_level": 1034.87,
                "grnd_level": 1030.97,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 20
            },
            "wind": {
                "speed": 3.36,
                "deg": 19.0017
            },
            "rain": {
                "3h": 0.0049999999999999
            },
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-22 09:00:00"
        },
        {
            "dt": 1519300800,
            "main": {
                "temp": 275.551,
                "temp_min": 275.551,
                "temp_max": 275.551,
                "pressure": 1031.73,
                "sea_level": 1035.71,
                "grnd_level": 1031.73,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                }
            ],
            "clouds": {
                "all": 44
            },
            "wind": {
                "speed": 3.64,
                "deg": 9.00037
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-22 12:00:00"
        },
        {
            "dt": 1519311600,
            "main": {
                "temp": 275.719,
                "temp_min": 275.719,
                "temp_max": 275.719,
                "pressure": 1031.73,
                "sea_level": 1035.64,
                "grnd_level": 1031.73,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 3.77,
                "deg": 348.506
            },
            "rain": {
                "3h": 0.01
            },
            "snow": {
                "3h": 0.005
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-22 15:00:00"
        },
        {
            "dt": 1519322400,
            "main": {
                "temp": 275.491,
                "temp_min": 275.491,
                "temp_max": 275.491,
                "pressure": 1030.82,
                "sea_level": 1034.72,
                "grnd_level": 1030.82,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 3.96,
                "deg": 345.006
            },
            "rain": {
                "3h": 0.16
            },
            "snow": {
                "3h": 0.1025
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-22 18:00:00"
        },
        {
            "dt": 1519333200,
            "main": {
                "temp": 275.089,
                "temp_min": 275.089,
                "temp_max": 275.089,
                "pressure": 1030.18,
                "sea_level": 1034.23,
                "grnd_level": 1030.18,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 4.07,
                "deg": 349.011
            },
            "rain": {
                "3h": 0.145
            },
            "snow": {
                "3h": 0.3
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-22 21:00:00"
        },
        {
            "dt": 1519344000,
            "main": {
                "temp": 275.492,
                "temp_min": 275.492,
                "temp_max": 275.492,
                "pressure": 1030.71,
                "sea_level": 1034.72,
                "grnd_level": 1030.71,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 3.11,
                "deg": 349.506
            },
            "rain": {
                "3h": 0.03
            },
            "snow": {
                "3h": 0.5375
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-23 00:00:00"
        },
        {
            "dt": 1519354800,
            "main": {
                "temp": 277.63,
                "temp_min": 277.63,
                "temp_max": 277.63,
                "pressure": 1029.18,
                "sea_level": 1033.11,
                "grnd_level": 1029.18,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 48
            },
            "wind": {
                "speed": 2.96,
                "deg": 0.000732422
            },
            "rain": {
                "3h": 0.0049999999999999
            },
            "snow": {
                "3h": 0.0050000000000001
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-23 03:00:00"
        },
        {
            "dt": 1519365600,
            "main": {
                "temp": 279.304,
                "temp_min": 279.304,
                "temp_max": 279.304,
                "pressure": 1027.82,
                "sea_level": 1031.7,
                "grnd_level": 1027.82,
                "humidity": 97,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 2.41,
                "deg": 0.500793
            },
            "rain": {
                "3h": 0.0049999999999999
            },
            "snow": {},
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-23 06:00:00"
        },
        {
            "dt": 1519376400,
            "main": {
                "temp": 277.384,
                "temp_min": 277.384,
                "temp_max": 277.384,
                "pressure": 1028.52,
                "sea_level": 1032.5,
                "grnd_level": 1028.52,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 2.11,
                "deg": 21.5013
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-23 09:00:00"
        },
        {
            "dt": 1519387200,
            "main": {
                "temp": 274.599,
                "temp_min": 274.599,
                "temp_max": 274.599,
                "pressure": 1029.03,
                "sea_level": 1033.12,
                "grnd_level": 1029.03,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 1.56,
                "deg": 75.5063
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-23 12:00:00"
        },
        {
            "dt": 1519398000,
            "main": {
                "temp": 273.464,
                "temp_min": 273.464,
                "temp_max": 273.464,
                "pressure": 1029.22,
                "sea_level": 1033.3,
                "grnd_level": 1029.22,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 1.28,
                "deg": 328.509
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-23 15:00:00"
        },
        {
            "dt": 1519408800,
            "main": {
                "temp": 273.88,
                "temp_min": 273.88,
                "temp_max": 273.88,
                "pressure": 1030.38,
                "sea_level": 1034.45,
                "grnd_level": 1030.38,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 3.8,
                "deg": 354.001
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-23 18:00:00"
        },
        {
            "dt": 1519419600,
            "main": {
                "temp": 274.964,
                "temp_min": 274.964,
                "temp_max": 274.964,
                "pressure": 1031.83,
                "sea_level": 1035.98,
                "grnd_level": 1031.83,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 5.41,
                "deg": 351.001
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-23 21:00:00"
        },
        {
            "dt": 1519430400,
            "main": {
                "temp": 278.354,
                "temp_min": 278.354,
                "temp_max": 278.354,
                "pressure": 1033.97,
                "sea_level": 1037.93,
                "grnd_level": 1033.97,
                "humidity": 89,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 3.47,
                "deg": 10.5009
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-24 00:00:00"
        },
        {
            "dt": 1519441200,
            "main": {
                "temp": 280.906,
                "temp_min": 280.906,
                "temp_max": 280.906,
                "pressure": 1032.84,
                "sea_level": 1036.66,
                "grnd_level": 1032.84,
                "humidity": 80,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 1.75,
                "deg": 106.004
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-24 03:00:00"
        },
        {
            "dt": 1519452000,
            "main": {
                "temp": 282.578,
                "temp_min": 282.578,
                "temp_max": 282.578,
                "pressure": 1030.23,
                "sea_level": 1034.16,
                "grnd_level": 1030.23,
                "humidity": 71,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ],
            "clouds": {
                "all": 20
            },
            "wind": {
                "speed": 3.21,
                "deg": 173.521
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-24 06:00:00"
        },
        {
            "dt": 1519462800,
            "main": {
                "temp": 280.056,
                "temp_min": 280.056,
                "temp_max": 280.056,
                "pressure": 1030.52,
                "sea_level": 1034.5,
                "grnd_level": 1030.52,
                "humidity": 79,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 2.36,
                "deg": 94.001
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-24 09:00:00"
        },
        {
            "dt": 1519473600,
            "main": {
                "temp": 277.846,
                "temp_min": 277.846,
                "temp_max": 277.846,
                "pressure": 1032.15,
                "sea_level": 1036.13,
                "grnd_level": 1032.15,
                "humidity": 96,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ],
            "clouds": {
                "all": 0
            },
            "wind": {
                "speed": 3.45,
                "deg": 54.0003
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-24 12:00:00"
        },
        {
            "dt": 1519484400,
            "main": {
                "temp": 277.727,
                "temp_min": 277.727,
                "temp_max": 277.727,
                "pressure": 1033.04,
                "sea_level": 1037.01,
                "grnd_level": 1033.04,
                "humidity": 95,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n"
                }
            ],
            "clouds": {
                "all": 20
            },
            "wind": {
                "speed": 4.71,
                "deg": 15.5038
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-24 15:00:00"
        },
        {
            "dt": 1519495200,
            "main": {
                "temp": 277.813,
                "temp_min": 277.813,
                "temp_max": 277.813,
                "pressure": 1032.82,
                "sea_level": 1036.74,
                "grnd_level": 1032.82,
                "humidity": 99,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n"
                }
            ],
            "clouds": {
                "all": 20
            },
            "wind": {
                "speed": 5.8,
                "deg": 15.5009
            },
            "rain": {},
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-24 18:00:00"
        },
        {
            "dt": 1519506000,
            "main": {
                "temp": 277.701,
                "temp_min": 277.701,
                "temp_max": 277.701,
                "pressure": 1033.7,
                "sea_level": 1037.59,
                "grnd_level": 1033.7,
                "humidity": 97,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 88
            },
            "wind": {
                "speed": 5.61,
                "deg": 5.50305
            },
            "rain": {
                "3h": 0.135
            },
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-24 21:00:00"
        },
        {
            "dt": 1519516800,
            "main": {
                "temp": 278.309,
                "temp_min": 278.309,
                "temp_max": 278.309,
                "pressure": 1035.24,
                "sea_level": 1039.16,
                "grnd_level": 1035.24,
                "humidity": 95,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 5.61,
                "deg": 11.5001
            },
            "rain": {
                "3h": 0.17
            },
            "snow": {},
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-25 00:00:00"
        },
        {
            "dt": 1519527600,
            "main": {
                "temp": 279.491,
                "temp_min": 279.491,
                "temp_max": 279.491,
                "pressure": 1033.08,
                "sea_level": 1037.04,
                "grnd_level": 1033.08,
                "humidity": 95,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 5.56,
                "deg": 9.50018
            },
            "rain": {
                "3h": 0.145
            },
            "snow": {},
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-25 03:00:00"
        },
        {
            "dt": 1519538400,
            "main": {
                "temp": 278.781,
                "temp_min": 278.781,
                "temp_max": 278.781,
                "pressure": 1031.09,
                "sea_level": 1034.87,
                "grnd_level": 1031.09,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 5.26,
                "deg": 11.5011
            },
            "rain": {
                "3h": 0.795
            },
            "snow": {},
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2018-02-25 06:00:00"
        },
        {
            "dt": 1519549200,
            "main": {
                "temp": 277.745,
                "temp_min": 277.745,
                "temp_max": 277.745,
                "pressure": 1028.89,
                "sea_level": 1032.68,
                "grnd_level": 1028.89,
                "humidity": 100,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 6.01,
                "deg": 13.0039
            },
            "rain": {
                "3h": 0.9
            },
            "snow": {},
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-02-25 09:00:00"
        }
        ],
        "city": {
            "id": 1850144,
            "name": "Tokyo",
            "coord": {
                "lat": 35.6828,
                "lon": 139.759
            },
            "country": "JP",
            "population": 12445327
        }
    }



    # weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=tokyo&APPID=f2f33dbceea19eef373a3972938b7cb1')
    # data =  weather.json()
    # print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["sys"]["sunset"]))
    # return render(request, "check/index.html", {"city": city, "weather": weather.json()})
    return render(request, "check/index.html",{"city":city})



