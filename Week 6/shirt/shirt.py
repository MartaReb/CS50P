import sys

def main():
    check_command_line_arguments()


def check_command_line_arguments():
    if len(sys.argv)< 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)> 3:
        sys.exit("Too many command-line arguments")
    else:
        name1, extension1 = sys.argv[1].split(".")
        name2, extension2 = sys.argv[2].split(".")
        if not ((extension1.lower() and extension2.lower()) in ["jpg", "jpeg", "png"]):
            sys.exit("Invalid output")
        elif not (extension1 == extension2):
            sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()