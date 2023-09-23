import random

def main():
    level = get_level()
    game(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in [1,2,3]:
                return level

def game(level):
    if level == 1:
        start = 0
        end = 9
    elif level == 2:
        start = 10
        end = 99
    else:
        start = 100
        end = 999

    score = 0
    for v in range(10):
        x = random.randint(start,end)
        y = random.randint(start,end)
        answer = x + y
        wrong_answer = 0
        while True:
            print(f"{x} + {y} = ", end="")
            try:
                user_answer = int(input())
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    wrong_answer += 1
                    if wrong_answer == 3:
                        print(answer)
                        break
            except ValueError:
                    print("EEE")
    print(score)