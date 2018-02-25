from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^weather-today/', views.weather_today,name="weather_today"),
]