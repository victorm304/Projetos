import time 

start = time.time()
# a = 3
# b = 4
# c = ((a**2) + (b**2)) ** 0.5
# produtoabc = a * b * c
produtoabc = 0

for a in range(1, 1000+1):
    for b in range(a,1000+1):
        c = ((a**2) + (b**2)) ** 0.5
        produtoabc = a + b + c
        if produtoabc == 1000:
            print(f'{a} * {b} * {c} = {a * b * c}')
            break

elapsed = time.time() - start               
print("Time: {:.5f} seconds".format(elapsed))