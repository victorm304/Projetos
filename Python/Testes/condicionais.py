# Simples, Composto, Encadeado

n1 = float(input("Digite um número: "))

if n1 == 10:
    print('O número é igual a 10')

# O elif apenas é considerado quando o if retorna False
elif n1 > 0:
    print ('O número e maior que zero')

# Este último elif apenas será executado se todos os anteriores retornarem False
elif n1 == 3:
    print ('O número é igual a 3')


