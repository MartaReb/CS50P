from datetime import date
import re
import inflect
import sys

p = inflect.engine()

def main():
    print(convert(input("Date of birth: ")))

def convert(d):
    time = re.search("^([1-2][0-9]{3})-([0-1][0-9])-([0-3][0-9])$", d)
    if time:
        year, month, day = time.groups()
        date_of_birth = date(int(year), int(month), int(day))
        current_date = date.today()
        time_difference = current_date - date_of_birth
        seconds_difference = int(time_difference.total_seconds()/60)
        words = (p.number_to_words(seconds_difference, andword="")).capitalize()
        return f"{words} minutes"
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()