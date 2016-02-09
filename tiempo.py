#-*- coding: utf-8 -*-
from pyql.weather.forecast import Forecast

woeid =  12578038 #numero de identificación de cada ciudad

forecast = Forecast.get(woeid=woeid, u="c")
ciudad = forecast.location.city #coje la ciudad, region y pais
region = forecast.location.region
pais = forecast.location.country
print("****************************************** ")
print("Condiciones del clima para la ciudad de {0}, {1}, {2}: \n".format(ciudad, region, pais))
print("*******************************************")
for day in forecast.item.forecast:
    print("Fecha: {0} {1}".format(day['day'], day['date']))
    print("Pronóstico: {0} ({1})".format(day['text'], day['code']))
    print("Temperatura Mínima: {0}º {1}".format(day['low'], forecast.units.temperature))
    print("Temperatura Máxima: {0}º {1}".format(day['high'], forecast.units.temperature))
    print("**********************************************************")

