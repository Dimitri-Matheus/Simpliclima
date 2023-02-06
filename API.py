# Módulos
import requests
from datetime import datetime
import pytz

def api_weather(city, temperature, weather, symbol):
    global zone_code

    # Funcionamento da API
    base_link = 'https://api.openweathermap.org/data/2.5/weather?'
    api_key = '11b6ad6dc2620a9ab8e73180a778f0b1'

    # A url do site
    url = base_link + 'appid=' + api_key + '&q=' + city

    # A resposta do site
    response = requests.get(url).json()

    # Convertendo kelvin para celsius
    def kelvin_to_celsius(kelvin):
        celsius = kelvin - 273
        return celsius


    temp_kelvin = response['main']['temp']  #temperatura kelvin
    temp_celsius = kelvin_to_celsius(temp_kelvin)   #temperatura celsius
    description = response['weather'][0]['description'] #descrição
    zone_code = response['sys']['country']  #código do país

    # As informações
    temperature.configure(text=f'{temp_celsius:.0f}')
    weather.configure(text=f'{description}'.replace('clouds', ''))
    symbol.configure(text='°C')


# Lógica das horas
def hour_main(place, day, night, evening):
    global zone_code

    zone = pytz.country_timezones[zone_code]    #zona
    date = pytz.timezone(zone[0])   #data
    hour = datetime.now(date)   #hora
    hour = hour.strftime('%H')    #tipo de hora
    hour_value = int(hour)

    # As informações
    if hour_value <= 5:
        place.configure(image=night)    #Imagem de noite
    elif hour_value <= 11:
        place.configure(image=day)  #Imagem de dia
    elif hour_value <= 17:
        place.configure(image=evening)  #Imagem de tarde
    elif hour_value <= 23:
        place.configure(image=night)

