from selenium import webdriver
from datetime import datetime, date, time

options = webdriver.ChromeOptions()
options.add_argument('headless')

today = datetime.today()

# start chrome browser
browser = webdriver.Chrome(
    executable_path='C:\\Users\\user1\\Desktop\\myScripts\\Python Scripts\\TelegaBot\\DCP\\chromedriver.exe', chrome_options=options)

browser.get('https://ru.tradingview.com/symbols/BTCUSD/')
value = browser.find_element_by_class_name(
    'tv-symbol-price-quote__value').text

""" print(value + str(' долларов стоит 1 btc на ' + str(today))) """

#Wrong change info, i'll try to fix it 
""" change = browser.find_element_by_class_name(
    'js-symbol-change-direction')

print(change.text + str(' изменения в стоимости')) """

browser.quit()
