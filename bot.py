import api
import db
import telebot

bot = telebot.TeleBot("5434796681:AAE2L-1SX3evqsgGZphxg-UQNCZrmyLombY", parse_mode=None)

@bot.message_handler(commands=['all'])
def all_w(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, "Сначала введите свой город😡")
    else:
        bot.send_message(message.chat.id, api.all_weather(shirota, dolgota))

bot.infinity_polling()