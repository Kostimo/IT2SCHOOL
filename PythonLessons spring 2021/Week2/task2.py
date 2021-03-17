A = [4, 8, 2, 4, 4, 6, 8, 2, 4, 2]
print(A)
B = set(A)
d = {}
for el in B:
    d[el] = A.count(el);
print(d)
    
