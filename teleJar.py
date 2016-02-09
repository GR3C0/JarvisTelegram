#-*- coding: utf:8 -*-

__autor__ = "Diego Morell"

#bot para telegram

import telebot #libreria del bot

TOKEN = "183411464:AAG6C72H-rshcfYp_-0dHLKfmLjiOIUrRJg" #Clave que la el grandioso BotFather

bot = telebot.TeleBot(TOKEN) # se combina la declaración del bot con la clave de API

def listener(mensajes):
	for m in mensajes:
		chat_id = m.chat.id
		texto = m.text
		print "ID: " + str(chat_id) + " - MENSAJE: " + texto
		if texto == "Hola":
			bot.send_message(chat_id, "Hola igualmente")
			bot.send_message(chat_id, "¿Cual es tu nombre?")
			chat_id = texto 
			print chat_id


"""def mensaje(mensaje):
	chat_id = mensaje.chat.id
	bot.send_message(chat_id, "Hola Mundo")"""

bot.set_update_listener(listener)
bot.polling(none_stop = True)