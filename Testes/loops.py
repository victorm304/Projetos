nome = None

while True:
    print('Digite seu nome, ou x para parar')
    nome = input()
    if nome == 'x' or nome == 'X':
        print('Encerrado')
        break

    print(f'Bem vindo, {nome}')


