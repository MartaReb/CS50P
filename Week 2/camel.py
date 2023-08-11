def main():
    camelCase = input("camelCase: ")
    print("snake_case: ",end="")
    snake_case(camelCase)

def snake_case(x):
    for letter in x:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter,end="")
main()