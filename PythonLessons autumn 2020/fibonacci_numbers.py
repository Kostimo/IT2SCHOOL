f1 = 0
f2 = 1
print(f"{f1} {f2} ", end="")
with open("fib_nums.txt", mode="w+") as fib_file:
    fib_file.write(f"{f1} {f2} ")
    for i in range(30):
        f3 = f1 + f2
        print(f"{f3} ", end="")
        fib_file.write(f"{f3} ")
        f1, f2 = f2, f3
    print(f"FILE: {fib_file.read()}")




