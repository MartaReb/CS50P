import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = re.search(r"^([0-9]+):?([0-9]*)?\s(AM|PM)\sto\s([0-9]+):?([0-9]*)?\s(AM|PM)$",s)
    if int(time.group(1)) < 13 or int(time.group(4)) < 13:
        if int(time.group(2)) < 60 or int(time.group(5)) < 60:
            return "valid"
    else:
        raise ValueError

if __name__ == "__main__":
    main()