import api
import db
import telebot

bot = telebot("5420997686:AAG6yf80LRLv3FjS8SbvDB_RfNg5BCiipjM")

@bot.message_handler(commands=['cloud'])
def get_cloud(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota = None:
        bot.send_message(message.chat.id, 'Сначала введите город')
    else
        bot.send_message(message.chat.id, api.cloudcover(shirota,dolgota))

bot.infinity_polling()
    