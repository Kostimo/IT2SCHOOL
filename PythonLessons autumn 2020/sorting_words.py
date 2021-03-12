with open("text.txt", mode="r") as text_file:
    text = text_file.read()
    split_text = text.split()
    with open("consonant.txt", mode="w") as consonant_file, open("vowel.txt", mode="w") as vowel_file, open("ali-words.txt", mode="w") as aliwords_file:
        for el in split_text:
            if el[0] in ("qwrtpsdfghjklzxcvbnmyQWRTPSDFGHJKLZXCVBNMY"):
                consonant_file.write(f"{el} ")
            else:
                vowel_file.write(f"{el} ")
            if el[0:3].lower() == "ali":
                aliwords_file.write(f"{el} ")
    



