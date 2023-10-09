import sys

def main():
    check_command_line_arguments()


def check_command_line_arguments():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()