import math
value=2
for i in range(3, 2000000):
        prime=True 
        if i%2 != 0:
            for j in range(3, int(round(math.sqrt(i)+1)),2):
                if i % j==0:
                    prime=False
        else:
            prime=False
        if prime==True:
            value+=i
print(value)