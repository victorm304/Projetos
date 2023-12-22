import httpx
import json

# Função para converter Kelvin para Celsius
def converter_para_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

if __name__ == '__main__':
    city_name = 'São Paulo'
    country_code = 'br'
    lang = 'pt_br'
    api_key = '032490db50ef4537bce870ec46b033ad'
    
    URL = httpx.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&lang={lang}&appid={api_key}')
    print(URL)
    result = URL.json()
    main = result.get('main', {})
    temperatura = int(converter_para_celsius(main['temp']))
    temperatura_min = int(converter_para_celsius(main['temp_min']))
    temperatura_max = int(converter_para_celsius(main['temp_max']))
    print(f'Temperatura: {temperatura}°C\nMínima: {temperatura_min}°C\nMáxima: {temperatura_max}°C')


   
    
    
    
    
