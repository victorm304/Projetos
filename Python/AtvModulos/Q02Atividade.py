# Lista com dicionários
pessoas = [{"nome": "joao", "idade": 25}, {"nome": "paulo", "idade": 54}, {"nome": "maria", "idade": 32}, {"nome": "marcos", "idade": 17}, {"nome": "jessica", "idade": 44}, {"nome": "isis", "idade": 22}, {"nome": "sofia", "idade": 18}] 

# Listas que serão armazenados os nomes e idades
nomes = []
idades = []

# Loop que percorre sobre a variável pessoas, e extrai o conteúdo dos nomes e das idades e adiciona cada um respecitvamente dentro das variaveis nomes e idades
for k in pessoas:
    nomes.append(k['nome'])
    idades.append(k['idade'])

# Imprime os resultados
print (f"Nomes: {nomes}")
print (f"Idades: {idades}")
       