def palindromo(num):
    numero_invertido = 0
    check = num
    while check != 0:
        digito = check % 10
        numero_invertido = (numero_invertido * 10) + digito
        check = check // 10
    if numero_invertido == num:
        return True
    else:
        return False

lista = []
for numero in range(100, 1000):
    for numero2 in range(100, 1000):
        calc = numero * numero2
        if palindromo(calc):
            lista.append(calc)

print(f'O resultado é: {max(lista)}')
