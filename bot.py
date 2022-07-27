import api
from db
import telebot

bot = telebot.TeleBot("5434796681:AAE2L-1SX3evqsgGZphxg-UQNCZrmyLombY", parse_mode=None)


@bot.message_handler(commands=['temp'])
def temp_w(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat_id)
    if shirota == None:
        bot.send_message(message.chat.id, 'Сначала введите свой город')
    else:
        bot.send_message(message.chat.id, api.temp_weather(shirota, dolgota))

bot.infinity_polling()