import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in [1,2,3]:
                return level

def generate_integer(level):
    if level == 1:
        start = 0
        end = 9
    elif level == 2:
        start = 10
        end = 99
    else:
        start = 100
        end = 999
    count = 0
    for v in range(10):
        x = random.randrange(start, end)
        y = random.randrange(start, end)
        answer = x + y
        print(f"{x} + {y} = ", end="")
        try:
            user_answer = int(input())
        except ValueError:
            print("EEE")
        else:
            if user_answer == answer:
                count += 1
            else:
                print("EEE")
    print(count)


if __name__ == "__main__":
    main()