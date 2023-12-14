# Funções lambda (anônimas)

# fahrenreit = lambda f: (f - 32) * 5/9

# print(fahrenreit(68))

# Função map()
# Sintaxe
# Map(função, iterável)

num = [1,2,3,4,5,6,7,8]
dobro = tuple(map(lambda x: x * 2, num))
print(dobro)
