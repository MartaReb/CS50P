while True:
    fraction = input("Fraction:")
    try:
        numerator, denominator = fraction.split("/")
        number = int(numerator) / int(denominator)
        if number <= 1:
            break
    except(ValueError, ZeroDivisionError):
        pass

percent = number * 100
percent = int(round(percent,0))

if percent in (1,0):
    print("E")
elif percent in (99,100):
    print("F")
else:
    print(f"{percent}%")