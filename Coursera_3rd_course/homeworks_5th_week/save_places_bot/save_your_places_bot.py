#!/usr/bin/env python
from collections import defaultdict
import telebot
from telebot import types


TOKEN = '802665822:AAFf93yEKOvuVUYIowsgJWbGFq2Ac2aIx24'
bot = telebot.TeleBot(TOKEN)

START, ADD, NAME, LOCATION, PHOTO = range(5)
USER_STATE = defaultdict(lambda: START)

def get_state(message):
    return USER_STATE[message.chat.id]

def update_state(message, state):
    USER_STATE[message.chat.id] = state


@bot.message_handler(commands=['start'])
def handle_welcome(message):
    bot.send_message(message.chat.id, text="Hi! I can save all places you're going to visit! Please, start to type with '/' !")


@bot.message_handler(commands=['add'])
def handle_add(message):
    bot.send_message(message.chat.id, text="Send me name of the place")
    update_state(message, NAME)


@bot.message_handler(func=lambda message: get_state(message) == NAME)
def handle_name(message):
    # сохранить имя
    bot.send_message(message.chat.id, text="Send me location")
    update_state(message, LOCATION)


@bot.message_handler(func=lambda message: get_state(message) == LOCATION)
def handle_location(message):
    # сохранить фото
    bot.send_message(message.chat.id, text="Send me photo")
    update_state(message, PHOTO)

@bot.message_handler(func=lambda message: get_state(message) == PHOTO)
def handle_location(message):
    # сохранить фото
    bot.send_message(message.chat.id, text="Congrats! We are save another one place!")
    update_state(message, START)


@bot.message_handler(commands=['reset'])
def handle_reset(message):
    # удалить все места
    bot.send_message(message.chat.id, text="We are will delete all of your places. Are you sure?")


@bot.message_handler(commands=['list'])
def handle_list(message):
    #  прислать список из 10 последних мест
    name, location, photo = range(3)
    bot.send_message(message.chat.id, text='hsh')


bot.polling()
