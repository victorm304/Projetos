fibonacci = 1
a = 1
b = 1
soma_dos_termos = 0

while fibonacci <= 4000000:
   fibonacci = (a + b)
   a = b
   b = fibonacci
   
   if fibonacci % 2 == 0:
      soma_dos_termos += fibonacci

print(f'O resultado é : {soma_dos_termos}')
      



