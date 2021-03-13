from random import randint
n = int(input("N: "))
A = []
for _ in range(n):
    num = randint(3, 7)
    A.append(num)
print(A)

for i in range(1, len(A)-1):
    if A[i] > A[i-1] and A[i] > A[i+1]:
        print(A[i])