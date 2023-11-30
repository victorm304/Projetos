import os
import sys



# Verifica se o número de argumentos é correto
if len(sys.argv) != 3:
    print("Argumento inválido, use: nomedoarquivo.py nomedoarquivo nomedodiretório ")
    sys.exit(1)

# Obtém os argumentos da linha de comando
nome_arquivo = sys.argv[1]
diretorio_busca = sys.argv[2]

resultados = []

# Percorre as diretórios em busca do arquivo
for diretorio_atual, sub_diretorios, arquivos in os.walk(diretorio_busca):
    for arquivo in arquivos:
        if arquivo == nome_arquivo:
            caminho_absoluto = os.path.abspath(os.path.join(diretorio_atual, arquivo))
            resultados.append(caminho_absoluto)

# Imprime os resultados
if resultados:
    print("Arquivo encontrado em:")
    for resultado in resultados:
        print(resultado)
else:
    print("O Arquivo não encontrado.")