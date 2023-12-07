import random

#print('Gerar cinco números aleatórios entre 1 e 50: \n')

# for k in range(5):
#     n = random.randint(1,50)
#     print(f'Número gerado: {n}')

# Gera números flutuantes entre 1 e 100
# valor = random.uniform(1,100)


# print(f'Número: {valor}')

L = [2,4,6,9,10,13,5,6,7,66,55,44,22,100,1400,1900,100000,22223232,1212]
# n = random.choice(L)
# print (f'Número escolhido: {n}')

# num = random.sample(L,3)

# print (f'Números extraidos: {num}')

#Embaralhar
print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lista e exibi-la: ')

num = random.shuffle(L)
print(L)




