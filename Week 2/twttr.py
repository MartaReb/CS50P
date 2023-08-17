user_input = input("Input: ")
print("Output:",end="")

for letter in user_input:
    if letter.lower() in ["a","e","i","o","u"]:
        user_input.replace(letter,"")
    else:
        print(letter,end="")