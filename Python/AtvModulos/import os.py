import os
import sys

# Verificar se o número de argumentos é válido
if len(sys.argv) != 3:
    print("Use: python3 nomedoarquivo.py nomedodiretorio nomedoarquivo")
    sys.exit(1)

# Obter o diretório e o nome do arquivo a partir dos argumentos da linha de comando
diretorio = sys.argv[1]
nome_do_arquivo = sys.argv[2]

# Obter o caminho absoluto do diretório
caminho_absoluto_diretorio = os.path.abspath(diretorio)

# Verificar se o diretório existe
if not os.path.exists(caminho_absoluto_diretorio) or not os.path.isdir(caminho_absoluto_diretorio):
    print(f"Diretório '{caminho_absoluto_diretorio}' não encontrado.")
    sys.exit(1)

# Percorrer os arquivos no diretório
for nome_arquivo in os.listdir(caminho_absoluto_diretorio):
    caminho_absoluto_arquivo = os.path.join(caminho_absoluto_diretorio, nome_arquivo)

    # Verificar se o arquivo desejado foi encontrado
    if nome_do_arquivo == nome_arquivo:
        print("Arquivo encontrado! Caminho absoluto:", caminho_absoluto_arquivo)
        sys.exit(0)

# Se o arquivo não for encontrado
print(f"Arquivo '{nome_do_arquivo}' não encontrado no diretório '{caminho_absoluto_diretorio}'.")
