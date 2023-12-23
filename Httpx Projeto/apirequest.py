import httpx
import json
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Função para converter Kelvin para Celsius
def converter_para_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def converter_para_quilometro(velocidade_ms):
    km_por_hora = velocidade_ms * 3.6
    return km_por_hora

if __name__ == '__main__':
    city_name = input("Digite o nome da cidade: ")
    country_code = 'br'
    lang = 'pt_br'
    api_key = '032490db50ef4537bce870ec46b033ad'
    
    URL = httpx.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&lang={lang}&appid={api_key}')
    print(URL)
    result = URL.json()

    # Obter dados sobre a cidade 
    sys = result.get('sys', {})
    pais = sys['country']
    cidade = result['name']
    
    #Obter informações de data e hora
    data_hora = datetime.now()
    atual = data_hora.strftime('%A, %H:%M')
    
    # Obter o tempo(nublado, ceu aberto, etc.)
    weather = result.get('weather', {})
    if weather:
        primeiro_tempo = weather[0]
        tempo = primeiro_tempo.get('description')
        print(f'Tempo: {tempo.title()}')
    else:
        print('Informações sobre o tempo não disponíveis')

    # Obter a temperatura
    main = result.get('main', {})
    temperatura = int(converter_para_celsius(main['temp']))
    temperatura_min = int(converter_para_celsius(main['temp_min']))
    temperatura_max = int(converter_para_celsius(main['temp_max']))
    umidade = main['humidity']
    print(f'Temperatura: {temperatura}°C\nMínima: {temperatura_min}°C\nMáxima: {temperatura_max}°C')
    print (f'Umidade: {umidade}%')
    
    # Obtem informações sobre o vento
    wind = result.get('wind', {})
    speed = int(converter_para_quilometro(wind['speed']))
    print(f'Vento: {speed} km/h')
    print(result)