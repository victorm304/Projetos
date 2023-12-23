import httpx
import json
from datetime import datetime, timedelta
import locale

# Configura o idioma para português do brasil, talvez seja necessário instalar o pacote de idiomas para português do brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Função para converter Kelvin para Celsius
def converter_para_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius,2)

# Função para converter metros por segundos para quilometros por hora
def converter_para_quilometro(velocidade_ms):
    km_por_hora = velocidade_ms * 3.6
    return round(km_por_hora,2)

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
    city_id = result.get('timezone', {})
    id = result.get('id')
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
    temperatura = converter_para_celsius(main['temp'])
    temperatura_min = converter_para_celsius(main['temp_min'])
    temperatura_max = converter_para_celsius(main['temp_max'])
    sensaçao_termica = converter_para_celsius(main['feels_like'])
    pressao_atmosferica = main['pressure']
    visibilidade = result.get('visibility')
    umidade = main['humidity']
    print(f'Temperatura: {temperatura}°C\nMínima: {temperatura_min}°C\nMáxima: {temperatura_max}°C\nSensação Térmica: {sensaçao_termica}°C')
    print (f'Pressão Atmosférica: {pressao_atmosferica} hPa')
    print (f'Umidade: {umidade}%')
    print (f'Visibilidade: {visibilidade} metros')
    
    
    # Obtem informações sobre o vento
    wind = result.get('wind', {})
    speed = converter_para_quilometro(wind['speed'])
    direcao = wind['deg']
    print(f'Vento: {speed} km/h')
    print(f'Direção: {direcao} graus')
    
    # Obtem informações sobre nuvens
    clouds = result.get('clouds')
    nuvens = clouds['all']
    print(f'Cobertura de Nuvens: {nuvens}%')

    # Obtem latitude e longitude
    coord = result.get('coord', {})
    lat = coord['lat']
    long = coord['lon']
    print(f'Longitude: {long}\nLatitude: {lat}')

   # Obtem o codigo de resposta
    codigo_resposta = result.get('cod')
    
    # Obtem o fuso horário


    

