def main():
    greeting = input("Greeting: ")
    value_in_dolars = value(greeting)
    print (f"${value_in_dolars}")

def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h") and greeting != "hello":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()