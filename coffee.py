water = 400
milk = 540
coffeebeans = 120
disposablecups = 9
money = 550


def printAll():
    print("The coffee machin has:")
    print(water, " of water ")
    print(milk, " of milk ")
    print(coffeebeans, " of cofee beans ")
    print(disposablecups, " of disposable cups ")
    print(money, " of money ")
    print("\n")


printAll()
while True:

    a = ''
    while not(a in ["buy", "fill", "take"]):
        a = input("Write action (buy, fill, take):\n> ")

    if a == 'buy':
        b = 0
        while not(b in ["1", "2", "3"]):
            b = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n> ")
        if b == '1':
            water -= 250
            milk -= 0
            coffeebeans -= 16
            disposablecups -= 1
            money += 4

        if b == '2':
            water -= 350
            milk -= 75
            coffeebeans -= 20
            disposablecups -= 1
            money += 7

        if b == '3':
            water -= 200
            milk -= 100
            coffeebeans -= 12
            disposablecups -= 1
            money += 6
        print("\n")
        printAll()

    if a == 'fill':
        water += int(input('Write how many ml of water do you want to add:\n> '))
        milk += int(input('Write how many ml of milk do you want to add:\n> '))
        coffeebeans += int(
            input('Write how many grams of coffee beans do you want to add:\n> '))
        disposablecups += int(
            input('Write how many disposable cups do you want to add:\n> '))
        print("\n")
        printAll()

    if a == 'take':
        print('I gave $', money)
        money = 0
        printAll()
    print("-------------------------------------------------------------------------------")

    c = ''
    while not(c in ["1", "2"]):
        c = input("Do you want t return again?\n 1 - exit, 2 - return:\n> ")
    if c == '1':
        break
    print("-------------------------------------------------------------------------------\n")
