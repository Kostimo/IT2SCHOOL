m = int(input("m: "))
n = int(input("n: "))

def NOD(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

c = NOD(m,n)
def NOK(a, b):
    return f"NOK: {a*b/c}"

print(NOK(m,n))