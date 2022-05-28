from django import template
import requests, json

register = template.Library()

BASE_URL = 'http://api.weatherapi.com/v1/current.json?'
API_KEY = '93cdc04724c54f7d8c8125245222805'
CITY_NAME = 'Cairo'
URL = f'{BASE_URL}q={CITY_NAME}"&key={API_KEY}'


@register.simple_tag
def get_weather():
    res = requests.get(URL)
    print(URL)
    return res.json()
