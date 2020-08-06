from selenium import webdriver
from datetime import datetime

def main(webdriver, datetime):
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

    global value
    value = BTCcurrency.find_element_by_class_name(
        'tv-symbol-price-quote__value').text

    global change
    change = BTCcurrency.find_element_by_class_name(
        'js-symbol-change-direction').text

    #print(value, 'долларов стоит 1 btc а также имеет такие',  change, str('изменения в стоимости'), 'на', str(today))


    browser.quit()


main(webdriver, datetime)