import requests
import random

def main():
    print("Try to guess all the countries' capitals. You have 5 chances.")
    body = get_data_from_api()
    number = 5 
    score = 0
    final_score = 0
    while number > 0:
        country_num = country_list(body)
        capital_name = capital_list(body, country_num)
        print("What is the capital? ")
        answer = input().strip()
        outcome = user_answer(answer, capital_name, score)
        if outcome == 1:
            final_score += 1
        number = number - 1
    
    print(f"Your final score is: {final_score}/5")

def get_data_from_api():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        body = response.json()
        return body
    else:
        print(f"Error while downloading data. Error code: {response.status_code}")

def country_list(body):
    country = []
    for c in body:
        if c.get("independent") is True:
            country.append(c["name"]["official"])
    country_num = random.randint(0, (len(country)))
    print(f"Country: {country[country_num]}")
    return country_num

def capital_list(body, country_num):
    capital = []
    for c in body:
        if c.get("independent") is True:
            capital.append(c.get("capital"))
    return str(capital[country_num])[2:-2]

def user_answer(answer, capital_name, score):
    if answer == capital_name:
        score += 1
        print(f"Yeah! That's right!")
    else:
        print(f"The right answer is {capital_name}.Try again!")
    print()
    return score

if __name__ == "__main__":
    main()
