# 10001st Primo
def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

contagem = 0
y = 0

while contagem < 10001:
    y += 1
    if primo(y):
        contagem += 1
        if (contagem == 6) or (contagem == 10) or (contagem == 100) or (contagem == 1000) or (contagem == 10001):
            print(f'nthPrime({contagem}): {y}')
