#-*- coding: utf:8 -*-

__autor__ = "Diego Morell"

#bot para telegram

import telebot #libreria del bot
from pyql.weather.forecast import Forecast #Libreria para imprimir el tiempo

woeid =  12578038 #numero de identificación de cada ciudad(modulo del tiempo)
TOKEN = "183411464:AAG6C72H-rshcfYp_-0dHLKfmLjiOIUrRJg" #Clave que la el grandioso BotFather

bot = telebot.TeleBot(TOKEN) # se combina la declaración del bot con la clave de API

def listener(mensajes):
	for m in mensajes:
		chat_id = m.chat.id # reconoce el chat_id del usuario
		texto = m.text #text el mensaje del usuario
		print "ID: " + str(chat_id) + " - MENSAJE: " + texto #imprime en la terminal los mensajes recibidos

		if texto == "Hola": # condicionales que segun la respuesta del usuario hace X cosas
			bot.send_message(chat_id, "Hola igualmente")

		elif texto == "Dime el tiempo":
			forecast = Forecast.get(woeid=woeid, u="c")
			ciudad = forecast.location.city #coje la ciudad, region y pais
			region = forecast.location.region
			pais = forecast.location.country
			bot.send_message(chat_id,"Condiciones del clima para la ciudad de {0}, {1}, {2}: \n".format(ciudad, region, pais))
			for day in forecast.item.forecast: #para cada dia imprimir el tiempo
    				bot.send_message(chat_id,"Fecha: {0} {1}".format(day['day'], day['date']))
    				bot.send_message(chat_id,"Pronóstico: {0} ({1})".format(day['text'], day['code']))
    				bot.send_message(chat_id,"Temperatura Mínima: {0}º {1}".format(day['low'], forecast.units.temperature))
    				bot.send_message(chat_id,"Temperatura Máxima: {0}º {1}".format(day['high'], forecast.units.temperature))

"""def mensaje(mensaje):
	chat_id = mensaje.chat.id
	bot.send_message(chat_id, "Hola Mundo")"""

bot.set_update_listener(listener)
bot.polling(none_stop = True)