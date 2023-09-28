def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    if not s[0:2].isalpha():
        return False
    if not s.isalnum():
        return False
    if s.startswith("0", 2):
        return False
    if s[-1].isalpha() and s[-2].isdigit():
        return False
    else:
        return True


if __name__ == "__main__":
    main()