import sys

def main():
    check_command_line_arguments()


def check_command_line_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()