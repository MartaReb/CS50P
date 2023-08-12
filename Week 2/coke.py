amont_due = 50

while amont_due > 0:
    print("Amount Due:", amont_due)
    insert_coin = int(input("Insert Coin:"))
    if insert_coin in [25, 10, 5]:
        amont_due -= insert_coin
    if amont_due <= 0:
        print('Change Owed:', abs(amont_due))