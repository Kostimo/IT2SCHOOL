from random import randint
n = int(input("N: "))
A = []
for _ in range(n):
    num = randint(0, 10)
    A.append(num)
print(A)

m = int(input("M: "))
B = []

for i in range(n):
    if i+m > n-1:
        B.insert((i+m)%(n-1)-1, A[i])
    else:
        B.insert(i+m, A[i])

print(B)

