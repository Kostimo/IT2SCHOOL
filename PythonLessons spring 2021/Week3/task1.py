from random import randint
n = int(input("N: "))
A = []
for _ in range(n):
    num = randint(3, 7)
    A.append(num)
print(A)

s = sum(A)/n
print("Average: ", s)
for el in A:
    if el > s:
        print(el, "larger")
    elif el < s:
        print(el, "less")
    else:
        print(el, "equal")

