def Encrypt(text):
    text = str.replace(text, "m", "5")
    text = str.replace(text, "M", "4")
    text = str.replace(text, "Q", "7")
    text = str.replace(text, "q", "3")
    text = str.replace(text, "A", "0")
    text = str.replace(text, "a", "$")
    text = str.replace(text, "o", "!")
    text = str.replace(text, "O", "@")

    return text

def Descrypt(text): 
    text = str.replace(text, "5", "m")
    text = str.replace(text, "4", "M")
    text = str.replace(text, "7", "Q")
    text = str.replace(text, "3", "q")
    text = str.replace(text, "0", "A")
    text = str.replace(text, "$", "a")
    text = str.replace(text, "!", "o")
    text = str.replace(text, "@", "O")

    return text


text = input("Enter a text : ")
encrypt = Encrypt(text)
descrypt = Descrypt(encrypt)

print("""The text was : {0}
After encrypt : {1}
After descrypt : {2}""".format(text, encrypt, descrypt))