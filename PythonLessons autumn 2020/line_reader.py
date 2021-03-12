answ = ""
with open("users_text.txt", mode="w+") as user_file:
    while True:
        answ = input("Enter your text or enter \"exit\" to exit: ")
        if answ.lower() != "exit":
             user_file.write(f"{answ}\n")
        else:
            break
    user_file.seek(0)
    user_text = user_file.readlines()
    print(user_text)
