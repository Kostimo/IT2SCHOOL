from random import randint
n = int(input("N: "))
m = int(input("M: "))

A = []
for _ in range(n):
    num = randint(0, 10)
    A.append(num)
print(A)

B = []
for _ in range(m):
    num = randint(0, 10)
    B.append(num)
print(B)

C = []
for el in A:
    if el in B:
        C.append(el)

print(C)