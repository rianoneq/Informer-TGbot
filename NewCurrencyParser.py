import time
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime


#DOLLAR
def DOLLAR(BeautifulSoup, get):

  today = datetime.today()

  dollar_url = 'https://quote.rbc.ru/ticker/59111'

  response = get(dollar_url)

  soup = BeautifulSoup(response.text, 'html.parser')

  div = soup.find("div", {"class" : "chart"})

  dollar_currency = div.find("div", {"class" : "chart__info"})

  global dollarNAME
  dollarNAME = dollar_currency.find("span",  {"class" : "chart__info__name"}).text

  global dollarVALUE
  dollarVALUE = dollar_currency.find("span", {"class" : "chart__info__sum"}).text

  global dollarSTOCKS
  dollarSTOCKS  = dollar_currency.find("span", {"class" : "chart__info__change chart__change"}).text

  #print(dollarNAME.strip(), dollarVALUE.strip(), dollarSTOCKS.strip(), today)


#EURO
def EURO(BeautifulSoup, get):  
  today = datetime.today()

  euro_url = 'https://quote.rbc.ru/ticker/72383'

  response = get(euro_url)  

  soup = BeautifulSoup(response.text, 'html.parser')

  div = soup.find("div", {"class" : "chart"})

  euro_currency = div.find("div", {"class": "chart__info"})

  global euroNAME
  euroNAME = euro_currency.find("span",  {"class": "chart__info__name"}).text

  global euroVALUE
  euroVALUE = euro_currency.find("span", {"class": "chart__info__sum"}).text

  global euroSTOCKS
  euroSTOCKS  = euro_currency.find("span", {"class" : "chart__info__change chart__change"}).text

  #print(euroNAME.strip(), euroVALUE.strip(), euroSTOCKS.strip(), today)

DOLLAR(BeautifulSoup, get)
EURO(BeautifulSoup, get)