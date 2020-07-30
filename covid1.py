from covid import Covid

#magic variable
covid = Covid(source="worldometers")

#get data about covid from magic variable
covid.get_data()

#list countries
countries = covid.list_countries()

#get country covid info(russia)
russia = covid.get_status_by_country_name("Russia")

#get country
country = russia['country']

#get confirmed cases
confirmed = russia['confirmed']

#get new cases
new_cases = russia['new_cases']

#get new deaths and total deaths
new_deaths = russia['new_deaths']
total_deaths = russia['deaths']
