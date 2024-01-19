# Obtem o número pitagorico
for a in range(1, 1000+1):
    for b in range(a,1000+1):
        c = ((a**2) + (b**2)) ** 0.5
        produtoabc = (a + b + c)
        if produtoabc == 1000:
            print(f'\n{a} + {b} + {c} = {produtoabc}')
            print(f'{a} * {b} * {c} = {a * b * c}')
            break
