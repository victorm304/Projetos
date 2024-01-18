def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 ) + 1):
        if num % i == 0:
            return False
    return True

x = 600851475143
fatores_primos = []

for J in range(2, int(x ** 0.5)):
    if eh_primo(J):
        while x % J == 0:
            fatores_primos.append(J)
            x //= J

maior_fator = fatores_primos[3]            
print(f'\nFatores Primos: {fatores_primos}\n\nO maior fator primo é, portanto: {maior_fator}\n')