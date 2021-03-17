from random import randint
A = []
for _ in range(10):
    num = randint(-10, 20)
    A.append(num)
print(A)


B = []
m = 0
k = 0
k_max = 1
for i in range(len(A)-1):
    if A[i] < A[i+1]:
        n = i + 1
        k += 1
    else:
        if k > k_max:
            k_max = k
            m_max = m
            n_max = n
        k = 0
        m = i+1     

print(A[m_max:n_max+1])
