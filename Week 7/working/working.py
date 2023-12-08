import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = re.search(r"^([0-9]+):?([0-9]*)?\s(AM|PM)\sto\s([0-9]+):?([0-9]*)?\s(AM|PM)$",s)
    if int(time.group(1)) < 13 or int(time.group(4)) < 13:
        if time.group(3) == "AM" and int(time.group(1)) == 12:
            new_hour1 = "00"
        else:
            new_hour1 = int(time.group(1))
        if time.group(6) == "AM" and int(time.group(4)) == 12:
            new_hour2 = "00"
        else:
            new_hour2 = int(time.group(4))
        if time.group(3) == "PM" and int(time.group(1)) != 12:
            new_hour1 = int(time.group(1)) + 12
        if time.group(6) == "PM" and int(time.group(4)) != 12:
            new_hour2 = int(time.group(4)) + 12
        if time.group(2) == "":
            new_minutes1 = "00"
        if time.group(5) == "":
            new_minutes2 = "00"
        elif int(time.group(2)) < 60 or int(time.group(5)) < 60:
            new_minutes1 = time.group(2)
            new_minutes2 = time.group(5)
        else:
            raise ValueError
        return f"{new_hour1:02}:{new_minutes1} to {new_hour2:02}:{new_minutes2}"
    else:
        raise ValueError
if __name__ == "__main__":
    main()
