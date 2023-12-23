import httpx
import json
from datetime import datetime, timedelta
import locale

# Configura o idioma para português do brasil, talvez seja necessário instalar o pacote de idiomas para português do brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Função para converter Kelvin para Celsius
def converter_para_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

# Função para converter metros por segundos para quilometros por hora
def converter_para_quilometro(velocidade_ms):
    km_por_hora = velocidade_ms * 3.6
    return km_por_hora

if __name__ == '__main__':
    
    while True:
        # Dados que serão utilizados na requisição da API
        city_name = input("Digite o nome da cidade: ")
        country_code = 'br'
        lang = 'pt_br'
        api_key = '032490db50ef4537bce870ec46b033ad'
        URL = httpx.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&lang={lang}&appid={api_key}')

        if URL.status_code == 200:
            result = URL.json()
            print(URL)
            break
        else:
            print(URL)
            print('Ocorreu um erro, tente novamente.')
    

    # Obter dados sobre a cidade 
    sys = result.get('sys', {})
    pais = sys['country']
    cidade = result['name']
    print(f'\nResultados para {cidade}, {pais}:\n')
    
    #Obter informações de data e hora
    data_hora = datetime.now()
    atual = data_hora.strftime('%A, %H:%M')
    print(atual.title())
    
    # Obter o tempo(nublado, ceu aberto, etc.)
    weather = result.get('weather', {})
    if weather:
        primeiro_tempo = weather[0]
        tempo = primeiro_tempo.get('description')
        print(f'Tempo: {tempo.title()}')
    else:
        print('Informações sobre o tempo não disponíveis')

    # Obter a temperatura, umidade, pressão atmosferica e visibilidade
    main = result.get('main', {})
    temperatura = int(converter_para_celsius(main['temp']))
    temperatura_min = int(converter_para_celsius(main['temp_min']))
    temperatura_max = int(converter_para_celsius(main['temp_max']))
    pressao_atmosferica = main['pressure']
    visibilidade = result.get('visibility')
    umidade = main['humidity']
    print(f'Temperatura: {temperatura}°C\nMínima: {temperatura_min}°C\nMáxima: {temperatura_max}°C')
    print (f'Pressão Atmosférica: {pressao_atmosferica} hPa')
    print (f'Umidade: {umidade}%')
    print (f'Visibilidade: {visibilidade} metros')
    
    
    # Obtem informações sobre o vento
    wind = result.get('wind', {})
    speed = int(converter_para_quilometro(wind['speed']))
    print(f'Vento: {speed} km/h')
    
    # Obtem informações sobre nuvens
    clouds = result.get('clouds')
    nuvens = clouds['all']
    print(f'Cobertura de Nuvens: {nuvens}%')

    # Obtem latitude e longitude
    coord = result.get('coord', {})
    lat = coord['lat']
    long = coord['lon']
    print(f'Longitude: {long}\nLatitude: {lat}')

    # Obtem informações sobre fuso horário
    

    

