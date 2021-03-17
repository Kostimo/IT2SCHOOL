m = int(input("m: "))
n = int(input("n: "))

def NOD(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a
 
def NOK(a, b):
    return f"NOK: {a*b/NOD(m,n)}"

print(NOK(m,n))