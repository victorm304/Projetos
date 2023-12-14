# num = int(input("Digite um número: "))

# numero_invertido = 0

# while num > 0:
#     ultimo_digito = num % 10
#     numero_invertido = (numero_invertido * 10) + ultimo_digito
#     num = num // 10

# print(numero_invertido)

def inverter_numero(numero):
    numero_invertido = 0
    while numero > 0:
        ultimo_digito = numero % 10
        numero_invertido = (numero_invertido * 10) + ultimo_digito
        numero = numero // 10
    return numero_invertido


if __name__ == '__main__':
    perg = inverter_numero(int(input("Digite um número: ")))
    print(f'Número invertido: {perg}')

    

