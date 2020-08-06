from covid import Covid
from datetime import datetime
import time

def covid(Covid, datetime):
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

  #print("Информация о коронке на ", today, 
                 #"Страна: ", country, 
                 #"Всего подтвержденно случаев: ", confirmed, 
                 #"Всего смертей: ", total_deaths, 
                 #"Сегодняшние заражения: ",  new_cases, 
                 #"Сегодняшние смерти: ", new_deaths)


covid(Covid, datetime)
#time.sleep(60*20)
