from random import randint
A = []
for _ in range(10):
    num = randint(3, 7)
    A.append(num)
print(A)

k = 0
d = {}
for i in range(len(A)):
    m = A[i]
    for l in range(len(A)):
        if A[l] == m:
            k+=1
    d[m] = k;
    k=0;


print(d)
    
