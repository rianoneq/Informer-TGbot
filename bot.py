import telebot
from datetime import *
from config import token
from telebot import types
from covid1 import country, russia, new_cases, new_deaths, total_deaths, confirmed
from NewCurrencyParser import dollar, dollarNAME, dollarVALUE, dollarSTOCKS
from NewCurrencyParser import euro, euroNAME, euroVALUE, euroSTOCKS
from DCP.btc import *

today = datetime.today()

# bot initialization
bot = telebot.TeleBot(token)

#main keyboard(visiable all the time)
@bot.message_handler(commands=['s', 'start'])
def welcomeAndKeyboard(message):
    # welcome message
    img = open('media\lambert.webp', 'rb')

    bot.send_sticker(message.chat.id, img)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    #main keyboard buttons
    firstBtn = types.KeyboardButton('CURRENCIES')
    extraBtn = types.KeyboardButton('COVID-RUSSIA')

    markup.add(firstBtn, extraBtn)

    bot.send_message(message.chat.id, 'Приветствую, мой повелитель, {0.first_name}. Твой любой приказ выполнит личный поставщик информации и доносчик {1.first_name}'.format
                     (message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

#inline keyboard
@bot.callback_query_handler(func=lambda call: True)
def inlineKeyboard(call):   
    
    if call.message:
        if call.data == 'DOLLAR':
            bot.send_message(call.message.chat.id, dollarNAME.strip() +
                             str('\nДоллар к рублю:  ') + dollarVALUE.strip() +
                             str('\nИзменение курса:  ') + dollarSTOCKS.strip())
        elif call.data == 'EURO':
            bot.send_message(call.message.chat.id, euroNAME.strip() +
                             str('\nЕвро к рублю:  ') + euroVALUE.strip() +
                             str('\nИзменение курса:  ') + euroSTOCKS.strip())
        elif call.data == 'BTC':
            bot.send_message(call.message.chat.id, value +' долларов стоит 1 btc а также имеет такие ' + change + 
                             str(' изменения в стоимости ') + 'на ' + str(today))
  

#main scrtpt 
@bot.message_handler(content_types=['text'])
def conversation(message):

    if message.chat.type == 'private':
        if message.text == 'CURRENCIES':
            #inline keyboard buttons
            markup3 = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("DOLLAR", callback_data='DOLLAR')
            item2 = types.InlineKeyboardButton("EURO", callback_data='EURO')
            item3 = types.InlineKeyboardButton("BTC", callback_data='BTC')

            markup3.add(item1, item2, item3)

            bot.send_message(message.chat.id, text='О какой валюте ты бы хотел узнать?', reply_markup=markup3)

        #covid info
        elif message.text == 'COVID-RUSSIA':
            bot.send_message(message.chat.id, 'Информация о коронке на ' + str(today) +
                 str("\nСтрана: " + str(country) + str(
                "\nВсего подтвержденно случаев: " + str(confirmed)) + str(
                "\nВсего смертей: " + str(total_deaths)) + str(
                "\nСегодняшние заражения: " + str(new_cases)) + str(
                "\nСегодняшние смерти: " + str(new_deaths))))
                
        
    #hi/bye
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, создатель')
        hi = open('media/hi.mp4', 'rb')
        bot.send_video(message.chat.id, hi)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
        bye = open('media/bye.mp4', 'rb')
        bot.send_video(message.chat.id, bye)


# Bot run
if __name__ == '__main__':
    bot.polling(none_stop=True)