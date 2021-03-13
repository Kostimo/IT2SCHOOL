from random import randint
A = []
for _ in range(10):
    num = randint(3, 7)
    A.append(num)
print(A)

B = []

for el in A:
    if el not in B:
        B.append(el)
print(B)