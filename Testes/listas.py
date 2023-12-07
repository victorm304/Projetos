# Lista: representa uma sequência de valores armazenado na memória

# Sintaxe: nome_lista = [valores]

n1 = [4,6,7,8,0,3]
n2 = [1,6,3,0,12,11]
valores = n1 + n2
# valores[0] = 9
# print(len(valores))
# print(sorted(valores, reverse=True))
# print(sum(valores))
# print(min(valores))
# print(max(valores))

# 
# print(valores)
# valores.pop(3)
# print(valores)
# valores.insert(3,21)
# print(valores)
# print(12 in valores)

bebidas = []

print('Digite o nome das suas 5 bebidas favoritas: ')
for k in range(1,6):
    bebida = str(input(f"\nBebida {k}: "))
    bebidas.append(bebida)

print(f'\nBebidas escolhidas: ')
bebidas.sort()
for elemento in bebidas:
    print (elemento)
    
print(f'\nSaúde!')
    