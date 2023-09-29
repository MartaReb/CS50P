def main():
    fraction = input("Fraction:")
    percent = convert(fraction)
    output = gauge(percent)
    print(output)

def convert(fraction):
    while True:
        try:
            numerator, denominator = fraction.split("/")
            number = int(numerator) / int(denominator)
            if number <= 1:
                percent = number * 100
                percent = int(round(percent,0))
                return percent
        except(ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage in (1,0):
        return "E"
    elif percentage in (99,100):
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()