from requests import get
from bs4 import BeautifulSoup
#DOLLAR
dollar_url = 'https://quote.rbc.ru/ticker/59111'

# return full page content
response = get(dollar_url)

#variable content
soup = BeautifulSoup(response.text, 'html.parser')

#return needed div
div = soup.find("div", {"class" : "chart"})

#return needed content
dollar_currency = div.find("div", {"class" : "chart__info"})

dollarNAME = dollar_currency.find("span",  {"class" : "chart__info__name"}).text

dollarVALUE = dollar_currency.find("span", {"class" : "chart__info__sum"}).text

dollarSTOCKS  = dollar_currency.find("span", {"class" : "chart__info__change chart__change"}).text

dollar = (dollarNAME, dollarVALUE, dollarSTOCKS)

#EURO
euro_url = 'https://quote.rbc.ru/ticker/72383'

# return full page content
response = get(euro_url)  

#variable content
soup = BeautifulSoup(response.text, 'html.parser')

#return needed div
div = soup.find("div", {"class" : "chart"})

# return needed content
euro_currency = div.find("div", {"class": "chart__info"})

euroNAME = euro_currency.find("span",  {"class": "chart__info__name"}).text

euroVALUE = euro_currency.find("span", {"class": "chart__info__sum"}).text

euroSTOCKS  = euro_currency.find("span", {"class" : "chart__info__change chart__change"}).text

euro = euroNAME, euroVALUE, euroSTOCKS

#print(dollarNAME.strip(), dollarVALUE.strip(), dollarSTOCKS.strip())
#print(euroNAME.strip(), euroVALUE.strip(), euroSTOCKS.strip())


