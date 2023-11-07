import sys
import csv

def main():
    check_command_line_arguments()
    create_a_new_file()

def check_command_line_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def create_a_new_file():
    students = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]
                students.append(({"first": first.lstrip(), "last": last, "house": house}))
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()
