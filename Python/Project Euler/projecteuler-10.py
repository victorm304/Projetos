def is_primo(num):
    if num < 2:
        return False
    for i in range(2,int(num ** (1/2)) + 1):
        if num % i == 0:
            return False
    return True

sum_primes = 0

for num in range(1, 2000000):
    if is_primo(num):
        sum_primes += num

print(f'somaDosPrimos: {sum_primes}')