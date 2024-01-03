def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numeros = [18671, 16033, 14159, 7583, 5569, 21523, 4643, 8753, 24359, 4919, 1523, 11701, 15259, 6113, 17909, 21277, 15241, 11813, 4441, 18131, 5393, 12671, 13229, 16253, 24229, 2341, 1871, 19927]

for num in numeros:
    if is_prime(num):
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo.")
