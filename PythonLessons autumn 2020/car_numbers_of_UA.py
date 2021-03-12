carNums1 = [ f"BH {str(i)}" for i in range(10, 100)]
carNums2 = [f"{el} {i}{j}" for el in carNums1 for i in "ETIOPAHKXCB" for j in "ETIOPAHKXCB"]
print(carNums2)