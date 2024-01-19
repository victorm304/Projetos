with open('grade.txt','r') as arquivo:
    conteudo = arquivo.read().split()
    print(conteudo[128])