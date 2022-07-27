import api
import db
import telebot
bot = telebot.TeleBot("5470137243:AAH8xEBtQeVFzn3zhAX9Ews8FDMt3AXO3yA", parse_mode=None)

@bot.message_handler(commands=['rain'])
def dojdick(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, "Сначала введите свой город👿")
    else:
        bot.send_message(message.chat.id, api.rainy_weather(shirota, dolgota))

bot.infinity_polling()