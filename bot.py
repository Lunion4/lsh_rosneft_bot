import requests
import telebot
from telebot import types
import api



bot = telebot.TeleBot(open('config.txt').readline())
shirota = 55
dolgota = 37


@bot.message_handler(commands=['all_weather'])
def all_weather(message):
    bot.send_message(message.chat.id,api.all_weather(shirota, dolgota))


@bot.message_handler(commands=['temperature_weather'])
def temperature_weather(message):
    bot.send_message(message.chat.id,api.temperature_weather(shirota, dolgota))


@bot.message_handler(commands=['wind'])
def wind(message):
    bot.send_message(message.chat.id,api.wind(shirota, dolgota))


@bot.message_handler(commands=['rainy_weather'])
def rainy_weather(message):
    bot.send_message(message.chat.id,api.rainy_weather(shirota, dolgota))


@bot.message_handler(commands=['cloudcover'])
def cloudcover(message):
    bot.send_message(message.chat.id,api.cloudcover(shirota, dolgota))


@bot.message_handler(commands=["start"])
def start(message):
    #keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).row(types.KeyboardButton(text='🌡'),types.KeyboardButton(text='🪁'),types.KeyboardButton(text='💧'),types.KeyboardButton(text='⛅')).add(types.KeyboardButton(text='All'))
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).row(types.KeyboardButton(text='/temperature_weather'),\
    types.KeyboardButton(text='/wind'),types.KeyboardButton(text='/rainy_weather'),types.KeyboardButton(text='/cloudcover')).add(types.KeyboardButton(text='/all_weather'))

    bot.send_message(message.chat.id, "Выберете из меню", reply_markup=keyboard)























bot.infinity_polling()
