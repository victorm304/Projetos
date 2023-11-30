import itertools

# Dicionário para armazenar endereços IP e listas de tamanhos de objeto
dicionario = {}

# Abrir o arquivo
with open('apache.logs.txt', 'r') as arquivo:
    # Iterar sobre cada linha do arquivo
    for linha in arquivo:
        # Remover espaços em branco no início e no final da linha
        linha = linha.strip()

        # Dividir a linha em partes usando espaços como delimitadores
        partes = linha.split()

        # Verificar se a linha possui elementos suficientes
        if len(partes) >= 9:
            # Obter o endereço IP 
            contagem_ip = partes[0]

            # Obter o tamanho do objeto (convertendo para inteiro)
            tamanho_objeto = int(partes[8])

            # Adicionar o tamanho do objeto à lista associada ao endereço IP no dicionário
            if contagem_ip not in dicionario:
                dicionario[contagem_ip] = [tamanho_objeto]
            else:
                dicionario[contagem_ip].append(tamanho_objeto)

# Imprime as primeiras 5 entradas do dicionário
for chave, valores in itertools.islice(dicionario.items(), 5):
    print(f'Endereço IP: {chave}, Tamanhos do objeto: {valores}')

# Imprime o número de endereços IP encontrados
numero_enderecos_ip = len(dicionario)
print(f'Número de endereços IP únicos: {numero_enderecos_ip}')
