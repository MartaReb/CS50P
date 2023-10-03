import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    name,extension = sys.argv[1].split('.')
    if extension != "py":
        sys.exit("Not a Python file")
    else:
        with open(sys.argv[1], "r") as file:
            lines_num = 0
            for line in file:
                lines_num += 1
            print(lines_num)
except FileNotFoundError:
    print("File does not exist")
