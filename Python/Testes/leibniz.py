def leibniz(n):
    soma = 0
    for i in range(n):
        termo = (-1) ** i / (2 * i + 1)
        soma += termo

    return soma * 4

termos = int(input("Digite o número de termos: "))

#Executar a função

pi = leibniz(termos)

# Mostra o resultado:

print(f'Valor de pi: {pi}')
