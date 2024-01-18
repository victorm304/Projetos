#1 + 2 + 3 + 4 + 5 ....
a = 0
b = 0
for k in range(1 ,100+1):
    a = a + k
    b = b + (k ** 2)

resultado = (a ** 2) - b  
print(f'Resultado: {resultado}')
    
  
