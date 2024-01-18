
num = 0

# O programa leva em torno de 10 segundos para encontrar o número, por se tratar de números muito grandes
k = 0
while True:
    k += 20      
    for i in range(1, 20+1):
        if  k % i != 0:
            break
    else:
        num = k
        print('Encontrado!')
        break
            
print(f'\nO menor número dívisivel por todos os números de 1 a 20 é:\n{num}')

            
        






# for i in range(1, 20 + 1):
#     if x % i != 0:
#         lista.append(False)
#     else:
#         lista.append(True)


# print(lista)