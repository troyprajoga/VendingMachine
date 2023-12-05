def menu():
    print("1: Coca Kala  ($4.50)")
    print("2: Bepsi      ($3.50)")
    print("3: Fonta      ($6.50)")
    print("4: Sprit      ($5.50)")
    print("0: Leave")

def vendingMachine():
    vending_machine = """
     _________________________
    |  ___   ___   ___   ___  |
    |                         |
    |     Vending Machine     |
    |                         |
    | | 1 | | 2 | | 3 | | 4 | |
    | |___| |___| |___| |___| |
    |_________________________|
    """
    print(vending_machine)
    menu()

bills = input("Input money separated by decimal point: (00.00)").split(".")
dollar = int(bills[0]) * 100
coins = int(bills[1]) + dollar


def convertCoins(coins):
    quarters = (coins / 25).__floor__()
    coins = coins % 25
    dimes = (coins / 10).__floor__()
    coins = coins % 10
    nickels = (coins / 5).__floor__()
    pennies = coins % 5
    return quarters, dimes, nickels, pennies



vendingMachine()

while True:
    option = int(input("Choose an option: "))
    if option == 1:
        print("You chose Coca Kala")
        coins -= 450
        convertCoins(coins)
    elif option == 2:
        print("You chose Bepsi")
        coins -= 450
        convertCoins(coins)
    elif option == 3:
        print("You chose Fonta")
        coins -= 450
        convertCoins(coins)
    elif option == 4:
        print("You chose Sprit")
        coins -= 450
        convertCoins(coins)
    elif option == 0:
        print("Bye!")
        convertCoins(coins)
        break
    else:
        print("Input a valid number.")
        pass




quarters, dimes, nickels,pennies = convertCoins(coins)
print(f"Here are your coins:\n Quarters: {quarters}\n Dimes: {dimes}\n Nickles: {nickels}\n Pennies: {pennies}\n")
