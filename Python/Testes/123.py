import random

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
numeros_primos = list()

for J in range(2, 100000):
    calc = eh_primo(J)
    if calc == True:
        numeros_primos.append(J)

numeros_aleatorios = list()

while len(numeros_aleatorios) < 27:
    numeros_aleatorios.append(random.choice(numeros_primos))

print(f'{len(numeros_aleatorios)} Números primos foram sorteados: {numeros_aleatorios}')