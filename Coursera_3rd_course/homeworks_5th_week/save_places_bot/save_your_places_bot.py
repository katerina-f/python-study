#!/usr/bin/env python
from collections import defaultdict
import telebot
from telebot import types
import token_bot
import googlemaps
import pprint
import time

bot = telebot.AsyncTeleBot(token_bot.TOKEN)
gmaps = googlemaps.Client(key=token_bot.key_map)

START, NAME, LOCATION, PHOTO, NEARBY = range(5)
USER_STATE = defaultdict(lambda: START)

types_list = ['restaurant', 'art_gallery', 'cafe', 'store', 'movie_theater', 'bar', 'museum', 'park']

cash = {}

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width = 2)
    buttons = [types.InlineKeyboardButton(text=t, callback_data=t) for t in types_list]
    keyboard.add(*buttons)
    return keyboard


def get_state(message):
    return USER_STATE[message.chat.id]


def update_state(message, state):
    USER_STATE[message.chat.id] = state

def check_location(message):
    if message.text:
        if message.text.startswith('/'):
            bot.send_message(message.chat.id, text="Had failed to fulfil a command. Write a new command")
            update_state(message, START)
        else:
            bot.send_message(message.chat.id, text="Send a location of the place")
        return False
    elif message.location:
        return True
    else:
        bot.send_message(message.chat.id, text="Send a location of the place")
        return False


@bot.callback_query_handler(func=lambda x: True)
def callback_handler(callback_query):
    type = callback_query.data
    message = callback_query.message
    cash['type'] = type
    print(cash)
    bot.send_message(message.chat.id, text='Send your location')
    update_state(message, NEARBY)
    print(USER_STATE)

@bot.message_handler(commands=['start'])
def handle_welcome(message):
    bot.send_message(message.chat.id, text="Hi! I can save all places you're going to visit! Please, start to type with '/' !")


@bot.message_handler(commands=['add'])
def handle_add(message):
    bot.send_message(message.chat.id, text="Send a name of the place")
    update_state(message, NAME)


@bot.message_handler(func=lambda message: get_state(message) == NAME)
def handle_name(message):
    # сохранить имя
    if message.text is not None:
        if message.text.startswith('/'):
            bot.send_message(message.chat.id, text="Had failed to fulfil a command. Write a new command")
            update_state(message, START)
        else:
            update_state(message, LOCATION)
            bot.send_message(message.chat.id, text="Send a location of the place")


@bot.message_handler(func=lambda message: get_state(message) == NEARBY)
@bot.message_handler(func=lambda message: get_state(message) == LOCATION)
@bot.message_handler(content_types=['location'])
def handle_location(message, type=None):
    if USER_STATE[message.chat.id] == 2:
        if check_location(message) == True:
            bot.send_message(message.chat.id, text="Send a photo or any text instead, if you don't have a photo.")
            update_state(message, PHOTO)

    if USER_STATE[message.chat.id] == 4:
        if check_location(message) == True:
            lon, lat = message.location.longitude, message.location.latitude
            places_nearby = gmaps.places_nearby(location=f'{lat},{lon}', radius=500, type=cash['type'])
            print(places_nearby)
            for place in places_nearby['results']:
                place_id = place['place_id']
                fields = ['name', 'formatted_address', 'website']
                place_details = gmaps.place(place_id=place_id, fields=fields)
                # bot.send_location(message.chat.id,location=f'{lat},{lon}')
                print(place_details)


@bot.message_handler(func=lambda message: get_state(message) == PHOTO)
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # сохранить фото
    if USER_STATE[message.chat.id] == 3:
        if message.photo:
            photo = message.photo
        elif message.text:
            photo = 'No photo'
        bot.send_message(message.chat.id, text="Congrats! We are save another one place!")
        update_state(message, START)



@bot.message_handler(commands=['reset'])
def handle_reset(message):
    # удалить все места
    bot.send_message(message.chat.id, text="We are will delete all of your places. Are you sure?")


@bot.message_handler(commands=['list'])
def handle_list(message):
    #  прислать список из 10 последних мест
    bot.send_message(message.chat.id, text='hsh')


@bot.message_handler(commands=['nearby'])
def handle_nearby(message):
    #  показать места вокруг
    keyboard = create_keyboard()
    bot.send_message(message.chat.id, text='Send a type of places', reply_markup=keyboard)

bot.polling()
