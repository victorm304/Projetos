def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numeros_primos = []

for num in range(1, 2000000+1):
    if primo(num):
        numeros_primos.append(num)

print(sum(numeros_primos))