A = [1,2,3,4,5,6,7,8,9,10]
m = int(input("M: "))
print(A)

def shift(lst, sh):
    x = len(lst) - (sh%len(lst))
    return lst[x:] + lst[:x]

print(shift(A, m))

