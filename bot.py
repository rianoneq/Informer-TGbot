import telebot
import time
import threading
import random
from config import token
from telebot import types
from datetime import datetime
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from covid import Covid

#covid parser
def covid(Covid, datetime):
    while True:
        today = datetime.today()

        covid = Covid(source="worldometers")

        covid.get_data()

        countries = covid.list_countries()
        
        global russia
        russia = covid.get_status_by_country_name("Russia")

        global country
        country = russia['country']

        global confirmed
        confirmed = russia['confirmed']

        global new_cases
        new_cases = russia['new_cases']

        global new_deaths
        new_deaths = russia['new_deaths']

        global  total_deaths 
        total_deaths = russia['deaths']

        time.sleep(60)
        #print('HAHAHAHAHAHAHAHAHH')

#time.sleep(60*20)

#DOLLAR
def DOLLAR(get, BeautifulSoup):
    while True:

        global today
        today = datetime.today()

        dollar_url = 'https://quote.rbc.ru/ticker/59111'

        response = get(dollar_url)

        soup = BeautifulSoup(response.text, 'html.parser')

        div = soup.find("div", {"class" : "chart"})

        dollar_currency = div.find("div", {"class" : "chart__info"})

        global dollarVALUE
        dollarVALUE = dollar_currency.find("span", {"class" : "chart__info__sum"}).text

        global dollarSTOCKS
        dollarSTOCKS  = dollar_currency.find("span", {"class" : "chart__info__change chart__change"}).text
                
        #print('dollar', dollarVALUE.strip(), dollarSTOCKS.strip(), today)
        time.sleep(5)  
    

#EURO
def EURO(get, BeautifulSoup):
    while True:

        global today
        today = datetime.today()

        euro_url = 'https://quote.rbc.ru/ticker/72383'

        response = get(euro_url)  

        soup = BeautifulSoup(response.text, 'html.parser')

        div = soup.find("div", {"class" : "chart"})

        euro_currency = div.find("div", {"class": "chart__info"})

        global euroVALUE
        euroVALUE = euro_currency.find("span", {"class": "chart__info__sum"}).text

        global euroSTOCKS
        euroSTOCKS  = euro_currency.find("span", {"class" : "chart__info__change chart__change"}).text
                
        #print('еuro', euroVALUE.strip(), euroSTOCKS.strip(), today)
        time.sleep(10)  

#bitcoin
def btc(webdriver, datetime):
    while True:
        global today
        today = datetime.today()

        #the first argument prevents the browser opening, the second removes the trash in the console
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--log-level=3')

        
        # start chrome browser
        browser = webdriver.Chrome(
            executable_path='C:\\Users\\user1\\Desktop\\myScripts\\Python Scripts\\TelegaBot\\DCP\\chromedriver.exe', options=options)

        browser.get('https://ru.tradingview.com/symbols/BTCUSD/')

        #block where info about btc course(value and change)
        BTCcurrency = browser.find_element_by_class_name(
            'js-last-price-block-value-row')

        global btcVALUE
        btcVALUE = BTCcurrency.find_element_by_class_name(
            'tv-symbol-price-quote__value').text

        global btcCHANGE
        btcCHANGE = BTCcurrency.find_element_by_class_name(
            'js-symbol-change-direction').text

        #print(btcVALUE, 'долларов стоит 1 btc а также имеет такие',  btcCHANGE, str('изменения в стоимости'), 'на', str(today))
        time.sleep(5)


#multiпоточность и парсеры тут, ущербно зато робит
d = threading.Thread(target=DOLLAR, args=(get, BeautifulSoup), daemon=True)
e = threading.Thread(target=EURO, args=(get, BeautifulSoup), daemon=True)  
btc = threading.Thread(target=btc, args=(webdriver, datetime), daemon=True)  
covid = threading.Thread(target=covid, args=(Covid, datetime), daemon=True)  
 
d.start()
e.start()
btc.start()
covid.start()


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
            bot.send_message(call.message.chat.id, str('Доллар\Рубль на ') + str(today) +
                             str('\nДоллар к рублю:  ') + dollarVALUE.strip() +
                             str('\nИзменение курса:  ') + dollarSTOCKS.strip())
        elif call.data == 'EURO':
            bot.send_message(call.message.chat.id, str('Евро\Рубль на ') + str(today) +
                             str('\nЕвро к рублю:  ') + euroVALUE.strip() +
                             str('\nИзменение курса:  ') + euroSTOCKS.strip())
        elif call.data == 'BTC':
            bot.send_message(call.message.chat.id, btcVALUE +' долларов стоит 1 btc а также имеет такие ' + btcCHANGE + 
                             str(' изменения в стоимости ') + 'на ' + str(today))
    
#russian rullete(why not?)
def rullete(random):

        global god_change
        god_change = random.randint(1, 2)
        global other_var_life
        other_var_life = random.randint(2, 3)
        global other_var_death
        other_var_death = random.randint(4, 5)

#main scrtpt 
@bot.message_handler(content_types=['text'])
def conversation(message):
    
    if message.chat.type == 'private':
        if message.text == 'CURRENCIES':
            #inline keyboard buttons
            markup3 = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton('DOLLAR', callback_data='DOLLAR')
            item2 = types.InlineKeyboardButton('EURO', callback_data='EURO')
            item3 = types.InlineKeyboardButton('BTC', callback_data='BTC')

            markup3.add(item1, item2, item3)

            bot.send_message(message.chat.id, text='О какой валюте ты бы хотел узнать?', reply_markup=markup3)

        #covid info
        elif message.text == 'COVID-RUSSIA':
            bot.send_message(message.chat.id, 'Информация о коронке на ' + str(today) +
                 str('\nСтрана: ' + str(country) + str(
                '\nВсего подтвержденно случаев: ' + str(confirmed)) + str(
                '\nВсего смертей: ' + str(total_deaths)) + str(
                '\nСегодняшние заражения: ' + str(new_cases)) + str(
                '\nСегодняшние смерти: ' + str(new_deaths))))

        #russian rullete(why not?)
        if message.text.lower() == 'рулетка':
            
            rullete(random)    

            if god_change == 1:
                bot.send_message(message.chat.id, '{0.first_name}, ты выжил, lucky'.format(
                    message.from_user, bot.get_me()), parse_mode='html')
                if other_var_life == 2:
                    lucky = open('media/lucky.mp4', 'rb')
                    bot.send_video(message.chat.id, lucky)         
                if other_var_life == 3:
                    lucky = open('media/good.mp4', 'rb')
                    bot.send_video(message.chat.id, lucky)

            if god_change == 2:
                bot.send_message(message.chat.id, '{0.first_name}, ты помер, f'.format(
                    message.from_user, bot.get_me()), parse_mode='html')   
                if other_var_death == 4:
                    f = open('media/f.mp4', 'rb')
                    bot.send_video(message.chat.id, f)         
                if other_var_death == 5:
                    f = open('media/shot.mp4', 'rb')
                    bot.send_video(message.chat.id, f)         
            
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