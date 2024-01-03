import random

def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
numeros_primos = list()
for k in range(1000):
    calc = primo(k)
    if calc == True:
        numeros_primos.append(k)

aleatorios = list()
for i in range(37):
    aleatorios.append(random.choice(numeros_primos))

print(f'{len(aleatorios)} Números foram escolhidos: {numeros_primos}')