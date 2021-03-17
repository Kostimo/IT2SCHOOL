n = int(input("N: "))
f1 = 0
f2 = 1
print(f1)
for _ in range(n - 1):
    (f1, f2) = (f1+f2, f1)
    print(f1)