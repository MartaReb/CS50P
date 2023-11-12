import sys
from PIL import Image, ImageOps

def main():
    check_command_line_arguments()
    create_a_new_image()


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

def create_a_new_image():
    try:
        img = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    img_new_size = ImageOps.fit(img, size)
    img_new_size.paste(shirt, shirt)
    img_new_size.save(sys.argv[2])

if __name__ == "__main__":
    main()
