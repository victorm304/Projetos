# Dados fornecidos
dados_clima = {
    'coord': {'lon': -43.9378, 'lat': -19.9208},
    'weather': [{'id': 803, 'main': 'Clouds', 'description': 'nublado', 'icon': '04n'}],
    'base': 'stations',
    'main': {'temp': 294.1, 'feels_like': 294.65, 'temp_min': 293.59, 'temp_max': 294.5, 'pressure': 1018, 'humidity': 92},
    'visibility': 4000,
    'wind': {'speed': 1.03, 'deg': 270},
    'clouds': {'all': 75},
    'dt': 1703285338,
    'sys': {'type': 2, 'id': 2086218, 'country': 'BR', 'sunrise': 1703232845, 'sunset': 1703280853},
    'timezone': -10800,
    'id': 3470127,
    'name': 'Belo Horizonte',
    'cod': 200
}

# Calculando a velocidade do vento em km/h
velocidade_m_s = dados_clima['wind']['speed']
velocidade_kmh = velocidade_m_s * 3.6

# Exibindo o resultado
print(f"A velocidade do vento em Belo Horizonte é de {velocidade_kmh:.2f} km/h.")
