import sys
import csv
from tabulate import tabulate

def main():
    check_command_line_arguments()
    print_pizza_table()

def check_command_line_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

def print_pizza_table():
    pizza_table = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizza_table.append(row)
            print(tabulate(pizza_table, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()