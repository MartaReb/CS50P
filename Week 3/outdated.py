months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date = input ("Date: ")

if "/" in date:
    month, day, year = date.split("/")
    if month in months_list:
        date = input ("Date: ")
elif "," in date:
    month_day, year = date.split(",")
    month, day = month_day.split(" ")
    if month in months_list:
        month = months_list.index(month)
        month += 1
    else:
        date = input ("Date: ")
else:
    date = input ("Date: ")

day=int(day)
month=int(month)
year=int(year)
if day > 31 or month > 12:
    date = input ("Date: ")

print(year, f"{month:02}",f"{day:02}", sep="-")