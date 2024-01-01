# Funções lambda (anônimas)

# fahrenreit = lambda f: (f - 32) * 5/9

# print(fahrenreit(68))

# Função map()
# Sintaxe
# Map(função, iterável)

# num = [1,2,3,4,5,6,7,8]
# dobro = tuple(map(lambda x: x * 2, num))
# print(dobro)

# Função filter()
# Sintaxe:
# filter(função, sequência)

# def pares(n):
#     return n % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9,10]

# z = list(filter(lambda y: y % 3 == 0, numeros))
# print(z)

# numeros = list(range(1,100))

# saida = list(filter(lambda y: y % 2 == 0, numeros))
# print(saida)

# Função reduce()
# Sintaxe
# reduce(função, sequência, valor_inicial)

from functools import reduce

# def mult(x,y):
#     return x * y

# numeros = list(range(1,7))

# saida = reduce(mult, numeros)
# print(saida)

# Soma cumulativa dos quadrados de valores, usando a expressão lambda.

numeros = [1,2,3,4]

total = reduce(lambda x, y: x**2 + y**2, numeros)

print(total)