# Dicionário para armazenar endereços IP e listas de tamanhos de objeto
dicionario = {}
lista = []

# Abre o arquivo
with open('apache.logs.txt', 'r') as arquivo:
    # Percorre sobre cada linha do arquivo
    for linha in arquivo:
        # Remover espaços em branco no início e no final da linha
        linha = linha.strip()

        # Divide a linha em partes usando espaços como delimitadores
        partes = linha.split()

        # Obtem o endereço IP 
        contagem_ip = partes[0]

        # Obter o tamanho do objeto
        tamanho_objeto = partes[9]

        # Adicionar o tamanho do objeto à lista associada ao endereço IP no dicionário
        if contagem_ip not in dicionario:
            dicionario[contagem_ip] = [tamanho_objeto]
        else:
            dicionario[contagem_ip].append(tamanho_objeto)

# Imprime as primeiras 5 entradas do dicionário
for chave, valores in list(dicionario.items())[:5]:
    print 
    print(f'Endereço IP: {chave}, Tamanhos do objeto: {valores}')

# Imprime o número de endereços IP encontrados
numero_enderecos_ip = len(dicionario)
print(f'Número de endereços IP únicos: {numero_enderecos_ip}')
