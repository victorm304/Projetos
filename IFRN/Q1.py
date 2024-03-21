import os
import time
from tqdm import tqdm

# Função para converter uma string em uma lista de valores ASCII correspondente aos caracteres da string
def ascii(arqOrigem):
    return [int(ord(x)) for x in arqOrigem ]

# Função para realizar a operação XOR entre os bytes do arquivo de origem e da palavra-passe
def XOR(arqOrigem, palavra_passe):
    palavra_passe = ascii(palavra_passe)
    arqDestino = []
    indice_palavraPasse = 0 # Variável que assumirá algum valor referente a algum índice de palavra_passe

    for byte in arqOrigem:
        if indice_palavraPasse >= len(palavra_passe):
            # Quando o indice se igual ou maior que o número de itens de palavra_passe, reinicia a contagem, assim garantindo que os elementos de palavra_passe possam ser acessados novamente
            indice_palavraPasse = 0   
        
        # Realiza o XOR entre o byte atual do arqdestino e o byte atual da palavra-passe
        arqDestino.append(byte ^ palavra_passe[indice_palavraPasse])
        
        indice_palavraPasse += 1  # Atualiza a posição do indice, assim na proxima rodada o proximo byte da palavra seja ser acessado.
    
    return arqDestino # Retorna os bytes cifrados

# Função principal do script, responsavel por ler os bytes do arq de origem, chamar as funções auxiliares, e escrever os bytes cifrados no arq de destino.
def cifrar_arquivo(arquivoOrigem, palavra_passe, nome_arqDestino):
    #Define o tamanho do bloco a ser lido em bytes
    tam_bytes = 4096 
    tamanho_total = os.path.getsize(arquivoOrigem)

    with open(arquivoOrigem, "rb") as arq_origem, open(nome_arqDestino, "wb") as arq_destino:
        with tqdm(total=tamanho_total, unit='B', unit_scale=True, desc='Progresso') as pbar:
            
            while True:
                bloco = arq_origem.read(tam_bytes)
                if not bloco:
                # Se não houver mais conteúdo para ler, quebra o loop
                    break
            
            # Aplica a operação XOR no bloco de bytes atual, e escreve-os no arq de destino
                bloco_cifrado = XOR(bloco, palavra_passe)
                arq_destino.write(bytes(bloco_cifrado))

                pbar.update(len(bloco))

if __name__ == "__main__":
    # Solicita ao usuário o arq de origem, arq de destino, e palavra-passe
    arquivoOrigem = input("Digite o nome do arquivo de origem(ex: arquivo.png): ")
    palavra_passe = input("Digite a palavra-passe: ")
    nome_arqDestino = input("Digite o nome do arquivo de destino: ")
    
    # Inicio da captura do tempo de execução do programa
    inicio = time.time()
    
    # Verifica se já existe algum arquivo com o nome do arquivo de destino no diretório atual
    if nome_arqDestino not in os.listdir():
        # Tenta executar a função principal com os parametros fonecidos pelo usuário, e trata as possíveis exceções
        try:
            if not palavra_passe:
                print("Palavra-passe não informada.")
                raise SystemExit

            if not nome_arqDestino:
                print("Nome de arquivo de destino não informado.")
                raise SystemExit

            # Chamando a funçãoc       
            cifrar_arquivo(arquivoOrigem, palavra_passe, nome_arqDestino)
            print("Operação realizada com sucesso.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado. Tente novamente.')
            raise SystemExit
        
        except IsADirectoryError:
            print(f'Erro, "{arquivoOrigem}" é um diretório, Tente novamente.')
            raise SystemExit
    else:
        print(f'Erro, já existe um arquivo com o nome "{nome_arqDestino}" no diretório atual. Tente novamente.')
        raise SystemExit
    
# Fim da captura do tempo de execução
    fim = time.time()
# Imprime para o usuário o tempo de execução do programa
print(f'Tempo de execução: {round(fim - inicio, 2)} segundos')