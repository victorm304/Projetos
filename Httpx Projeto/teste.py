import httpx
import json

city_name = 'Rio de janeiro'
country_code = 'br'
lang = 'pt_br'
api_key = '032490db50ef4537bce870ec46b033ad'


URL = httpx.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&lang={lang}&appid={api_key}')
result = URL.json()
print(result['weather'])
print(result['dt'])