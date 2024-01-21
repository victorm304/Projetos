with open('p13-numerogrande.txt', 'r') as arquivo:
    numero = arquivo.read().split()
    soma = 0
    for num in numero:
        soma += int(num)

    resultado_soma = str(soma)
    dez_digitos = 0
    for J in resultado_soma:
        dez_digitos = (dez_digitos * 10) + int(J)
        if dez_digitos == int(resultado_soma[0:10]):
            print(f'Resultado: {dez_digitos}')
            break
