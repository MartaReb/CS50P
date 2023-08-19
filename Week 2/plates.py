def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:1].isalpha():
        if len(s) >=2 and len(s)<=6:
            if s[2] != "0":
                if s.isalnum():
                    if (s[-1].isdigit() and s[-2].isdigit()) or (s[-1].isalpha() and s[-2].isalpha()):
                        return True

main()