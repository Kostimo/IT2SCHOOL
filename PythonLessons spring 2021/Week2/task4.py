A = []
print("Enter \"x\" to exit.")
while True:
    print("num: ", end="")
    num = input()
    if num == "x":
        break
    else:
        if num not in A:
            A.append(num)
            print("Not occured")
        else:
            print("Occured")
