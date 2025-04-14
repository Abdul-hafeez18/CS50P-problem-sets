amount=50
change=0
print("Amount Due:", amount)
while amount>0:
    coin=int(input("Insert Coin:"))
    if coin == 25 or coin == 10 or coin ==5:
        amount = amount - coin
        change = change + coin
    if amount>0:
        print("Amount Due:", amount)
print("Change Owed:", change-50)