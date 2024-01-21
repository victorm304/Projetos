<<<<<<< HEAD
# Obtem o número pitagorico
for a in range(1, 1000):
    for b in range(a, 1000):
        c = ( (a ** 2) + (b ** 2) ) ** (1/2)
        produtoabc = a + b + c
        triplo_pitagorico = a * b * c
=======

for a in range(1, 1000):
    for b in range(a,1000):
        c = ((a**2) + (b**2)) ** 0.5
        produtoabc = (a + b + c)
>>>>>>> a36f005 (.)
        if produtoabc == 1000:
            print(f'triploPitagorico({produtoabc}): {triplo_pitagorico}')
            break