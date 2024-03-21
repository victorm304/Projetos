import hashlib
import time

# Função principal do script, chama as funções auxiliares e tenta encontrar o Nonce
def findNonce(dataToHash, bitsToBeZero):
    Nonce = 0

    # Inicio da captura do tempo execução do programa
    inicio = time.time()
    # Loop while para tentar encontrar o hash resultante, em quanto o Nonce for menor que 2 ^ 32 que é o tamanho maximo que um conjunto de 4 bytes pode comportar
    while Nonce <= (2 ** 32):
        # Aloca o Nonce na forma de 4 Bytes e concatena com os Bytes de entrada, e calcula o hash
        resultadoHash = calcular_hash(Nonce.to_bytes(4, 'big') + dataToHash)
        bitsZero = bits_zero_iniciais(resultadoHash)  # Chama a a outra função para verificar a qtde de bits zero iniciais no hash
        
        if bitsZero == bitsToBeZero:
            # Retorna o Nonce encontrado e o tempo de execução, assim que algum hash com a quantidade de bits zero iniciais definida pelo parametro BitsToBeZero
            fim = time.time()    # Fim da captura do tempo de execução
            return f"Nonce: {Nonce}\nTempo de execução: {round(fim - inicio, 2)} Segundos"
        
        Nonce += 1
    
    # Notifica ao usuário que não foi possível encontrar o Nonce especifico destes bytes de entrada
    return f'Não foi possível encontrar o Nonce para este conjunto de bytes de entrada.'

# Função para calcular o hash
def calcular_hash(conjuntoDeBytes):
    algoritmo = hashlib.sha256()
    algoritmo.update(conjuntoDeBytes)
    return algoritmo.digest()  # Retorna o hash obtido

# Função para calcular os bits zero iniciais
def bits_zero_iniciais(resultadoDoHash):
    bitsZero = 0
    for byte in resultadoDoHash: # Percorre sobre todos os bytes do hash obtido
        if byte == 0:
            bitsZero += 8    # Adicionar 8 bits para um byte 0
        else:
            bit = 0b10000000
            while byte & bit == 0:  # Aplica a operação booleana and para verificar a quantidade de bits zero iniciais em um byte, encerrando assim que um bit diferente de 0 for encontrado
                bitsZero += 1
                bit >>= 1   # Desloca os bits da variavel bit para que o proximo bit do Hash possa ser verificado na operação and
            
            break  # Encerra o loop for assim que  o loop while for encerrado
    
    return bitsZero

if __name__ == "__main__":
    Entrada = "Esse é fácil"
    # Solicita ao usuário o numero de bits zero iniciais necessários no hash
    qtd_ZerosIniciais = int(input("Digite o numero de bits iniciais que deve ser zero no hash: "))
    # Obtem os bytes de Entrada
    bytesDeEntrada = Entrada.encode('utf-8')

    print(findNonce(bytesDeEntrada, qtd_ZerosIniciais)) # Executa a função principal
