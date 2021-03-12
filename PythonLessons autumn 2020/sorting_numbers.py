from random import randint
with open("random_numbers.txt", mode="w+") as r_num:
    for i in range(1,1001):
        nums = randint(1,1001)
        r_num.write(f"{nums} ")
    r_num.seek(0)
    nums = r_num.read()
    lst_nums = nums.split()
    lst_nums = [int(i) for i in lst_nums]

    with open("on2.txt", mode="w") as on2_file, open("on3.txt", mode="w") as on3_file, open("on5.txt", mode="w") as on5_file, open("on10.txt", mode="w") as on10_file:
        for el in lst_nums:
            if el%2 == 0:
                on2_file.write(f"{el} ")
            if el%3 == 0:
                on3_file.write(f"{el} ")
            if el%5 == 0:
                on5_file.write(f"{el} ")
            if el%10 == 0:
                on10_file.write(f"{el} ")