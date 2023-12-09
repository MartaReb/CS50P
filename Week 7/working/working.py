import re

def main():
        print(convert(input("Hours: ")))

def convert(s):
    regex = "([0-9]+):?([0-9]*)? (AM|PM)"
    time = re.search(r"^" + regex + " to " + regex + "$",s)

    if time:
        new_hour1 = convert_hour(time.group(1), time.group(3))
        new_hour2 = convert_hour(time.group(4), time.group(6))
        new_minutes1 = convert_minutes(time.group(2))
        new_minutes2 = convert_minutes(time.group(5))
        return f"{new_hour1:02}:{new_minutes1} to {new_hour2:02}:{new_minutes2}"
    else:
        raise ValueError

def convert_hour(hour, period):
    hour = int(hour)
    if hour < 13:
        if period == "AM" and hour == 12:
            return 0
        elif period == "PM" and hour != 12:
            return hour + 12
        else:
            return hour
    else:
        raise ValueError

def convert_minutes(minutes):
    if minutes == "":
        return "00"
    elif int(minutes) < 60:
        return minutes
    else:
        raise ValueError

if __name__ == "__main__":
    main()
