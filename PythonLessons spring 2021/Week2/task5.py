from random import uniform
A = []
for _ in range(10):
    num = round(uniform(-10, 20), 5)
    A.append(num)
print(A)

k = 0 # Кол-во чисел в возрастающей последовательности
B = []
for i in range(len(A)-1):
    if A[i] < A[i+1]:
        k+=1
    else:
        B.append(k+1)
        k = 0

print(max(B))
