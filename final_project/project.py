import requests
import random

def main():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    body = response.json()
    capital_name = country_and_capital_list(body)

    print("What is the capital?")
    answer = input()
    if answer == capital_name:
        print("Yeah! That's right!")
    else:
        print("Try again")
        print(capital_name)

def country_and_capital_list(body):
    country = [c['name']['official'] for c in body]
    capital = [c.get('capital') for c in body]
    country_num = random.randint(0, (len(country)))
    print(country[country_num])
    return str(capital[country_num])[2:-2]

if __name__ == "__main__":
    main()
