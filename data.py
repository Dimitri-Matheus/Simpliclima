# Módulos
import requests
from datetime import datetime
import pytz

def api_weather(city):
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

    # A temperatura
    temp_kelvin = response['main']['temp']
    temp_celsius = kelvin_to_celsius(temp_kelvin)

    # A descrição
    description = response['weather'][0]['description']

    # O código do país
    zone_code = response['sys']['country']

    # A zona
    zone = pytz.country_timezones[zone_code]

    # A data
    date = pytz.timezone(zone[0])

    # A hora
    hour = datetime.now(date)
    hour = hour.strftime('%H:%M %p')

    # As informações
    print(f'A temperatura em {city}: {temp_celsius:.0f}°C')
    print(f'O clima geral em {city}: {description}')
    print(f'A hora em {city}: {hour}')


# Programa principal
api_weather('London')
