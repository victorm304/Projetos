# Obtem o número pitagorico
for a in range(1, 1000):
    for b in range(a, 1000):
        c = ( (a ** 2) + (b ** 2) ) ** (1/2)
        produtoabc = a + b + c
        triplo_pitagorico = a * b * c
        if produtoabc == 1000:
            print(f'triploPitagorico({produtoabc}): {triplo_pitagorico}')
            break