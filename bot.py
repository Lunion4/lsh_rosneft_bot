import api
import db
import telebot
bot = telebot.TeleBot("5434796681:AAE2L-1SX3evqsgGZphxg-UQNCZrmyLombY", parse_mode=None)


@bot.message_handler(func=lambda msg:msg.text=='Привет')
def hello_key(message):
    bot.send_message(message.chat.id, "Я приветствую тебя, дорогой мой друг!")
    bot.send_video(message.chat.id, "https://acegif.com/wp-content/gifs/privet-55.gif")
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).row(telebot.types.KeyboardButton(text='/start'))
    bot.send_message(message.chat.id, "Тыкните старт", reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def welcome(message):
    
    mesg = bot.send_message(message.chat.id, "Дражайше прошу Вас ввести город, в котором Вы находитесь.")
    bot.register_next_step_handler(mesg, save_city)
    

def save_city(message):
    if db.save_user_city(message.chat.id, message.text):
        bot.send_message(message.chat.id, "Большое спасибо, я польщён!")
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).row(telebot.types.KeyboardButton(text='🌡'),\
        telebot.types.KeyboardButton(text='🌪'),telebot.types.KeyboardButton(text='🌧'),telebot.types.KeyboardButton(text='☁️')).add(telebot.types.KeyboardButton(text='🌏'), telebot.types.KeyboardButton(text='Сменить город')) 
        bot.send_message(message.chat.id, "Выберите из меню: \n 🌡 температурка \n 🌪 ветерок\n 🌧 осадки \n ☁️ тучки\n 🌏 полный прогноз", reply_markup=keyboard)

    else:
        bot.send_message(message.chat.id, "Уважаемый, к сожалению, моя база данных еще маленькая, и ваш город я не нашел... Может Вас заинтересует, например, город Шуя")
        bot.register_next_step_handler(message, save_city)

@bot.message_handler(func=lambda msg:msg.text=='Сменить город')
def change_city(message):
    welcome(message)


@bot.message_handler(func=lambda msg:msg.text=='🌪')
def wind_w(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, 'Великопочтенный пользователь, я прошу Вас сначала ввести Ваш город!')
    else:
        bot.send_message(message.chat.id, api.wind(shirota, dolgota))
        
@bot.message_handler(func=lambda msg:msg.text=='🌡')
def temp_w(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, 'Великопочтенный пользователь, я прошу Вас сначала ввести Ваш город!')
    else:
        bot.send_message(message.chat.id, api.temperature_weather(shirota, dolgota))

@bot.message_handler(func=lambda msg:msg.text=='🌧')
def dojdick(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, "Великопочтенный пользователь, я прошу Вас сначала ввести Ваш город!")
    else:
        bot.send_message(message.chat.id, api.rainy_weather(shirota, dolgota))

@bot.message_handler(func=lambda msg:msg.text=='☁️')
def get_cloud(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, 'Великопочтенный пользователь, я прошу Вас сначала ввести Ваш город!')
    else:
        bot.send_message(message.chat.id,api.cloudcover(shirota,dolgota))

@bot.message_handler(func=lambda msg:msg.text=='🌏')
def all_w(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, "Великопочтенный пользователь, я прошу Вас сначала ввести Ваш город!")
    else:
        
        bot.send_message(message.chat.id,db.get_user_city(message.chat.id)+'\n'+  api.all_weather(shirota, dolgota))

@bot.message_handler(commands=['pressure'])
def grandmother(message):
    shirota, dolgota = db.get_user_lon_lat(message.chat.id)
    if shirota == None:
        bot.send_message(message.chat.id, 'Великопочтенный пользователь, я прошу Вас сначала ввести Ваш город!')
    else:
        bot.send_message(message.chat.id, api.pressure(shirota,dolgota))
        bot.send_video(message.chat.id, api.rand_img())

@bot.message_handler(commands=['meme'])
def grandmother(message):
    bot.send_video(message.chat.id, api.rand_meme())

bot.infinity_polling()


