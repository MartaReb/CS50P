from validator_collection import validators

def main():
    user_input = input("What's your email address? ")

    try:
        email_address = validators.email(user_input)
        print("Valid")
    except:
        print("Invalid")
if __name__ == "__main__":
    main()