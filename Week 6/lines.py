import sys

def main():
    check_command_line_arguments()
    count_lines()


def check_command_line_arguments():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
    except FileNotFoundError:
        print("File does not exist")

def count_lines():
    with open(sys.argv[1], "r") as file:
        lines_num = 0
        # loop through the lines to check if starts with # or whitespace
        for line in file:
            if not (line.lstrip().startswith("#") or line.isspace()):
                lines_num += 1
    print(lines_num)

if __name__ == "__main__":
    main()
