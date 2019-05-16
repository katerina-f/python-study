#!/usr/bin/env python

import telebot
from telebot import types

TOKEN = '802665822:AAFf93yEKOvuVUYIowsgJWbGFq2Ac2aIx24'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def add_place():
    pass


@bot.message_handler(commands=['start'])
def handle_welcome(message):
    bot.send_message(message.chat.id, text="Hi! I can save all places you're going to visit! Please, start to type with '/' !")

bot.polling()
