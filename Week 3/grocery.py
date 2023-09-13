grocery_list = {}
while True:
    try:
        product = input().upper()
        if product not in grocery_list:
            grocery_list[product] = 1
        else:
            grocery_list[product] += 1
    except EOFError:
        for product, value in sorted(grocery_list.items()):
            print(value, product)
        break
