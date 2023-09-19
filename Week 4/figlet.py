import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    random_font = random.choice(font_list)
    f = Figlet(font = random_font)
elif len(sys.argv) == 3 and sys.argv[2] in font_list and sys.argv[1] in ["-f", "--font"]:
    f = Figlet(font = sys.argv[2])
else:
    sys.exit("Invalid usage")

user_input = input("Input: ")
print ("Output: ")
print(f.renderText(user_input))