from random import randint
n = int(input("N: "))
m = int(input("M: "))

A = [randint(0,10) for _ in range(n)]
print(A)

B = [randint(0,10) for _ in range(m)]
print(B)

C = list(set(A) & set(B))
print(C)