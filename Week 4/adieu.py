import inflect
p = inflect.engine()
names_list = []

while True:
    try:
        name = input("Name: ")
        names_list.append(name)
    except EOFError:
        break
names = p.join(names_list)
print("Adieu, adieu, to", names)