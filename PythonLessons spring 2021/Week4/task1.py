m = int(input("m: "))
n = int(input("n: "))

def NOD(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return f"НОД: {a}"

print(NOD(m,n))