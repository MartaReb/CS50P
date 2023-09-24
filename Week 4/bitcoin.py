import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    bitcoin_amount = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    bitcoin_price = o["bpi"]["USD"]["rate_float"]
    amount = bitcoin_amount * bitcoin_price
    print(f"${amount:,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("Request Exception")