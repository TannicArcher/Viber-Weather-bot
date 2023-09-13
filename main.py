import requests
import time
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage

# Ваши данные для Viber Bot
bot_configuration = BotConfiguration(
    name='WeatherBot',
    avatar='https://example.com/avatar.jpg',
    auth_token='YOUR_AUTH_TOKEN'
)
viber_api = Api(bot_configuration)

# Ваши данные для API погоды
weather_api_key = 'YOUR_WEATHER_API_KEY'
city_name = 'YOUR_CITY_NAME'

def get_weather():
    url = f'http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city_name}'
    response = requests.get(url)
    data = response.json()
    current_temp = data['current']['temp_c']
    condition = data['current']['condition']['text']
    return f'Current weather in {city_name}: {current_temp}°C, {condition}'

def send_weather_message():
    weather_message = get_weather()
    viber_api.send_messages('YOUR_USER_ID', [TextMessage(text=weather_message)])

while True:
    send_weather_message()
    time.sleep(5 * 60 * 60)  # Ожидание 5 часов до следующего обновления
