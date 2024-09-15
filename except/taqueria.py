menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main ():
    x = get_total()
    print(f"\nTotal: ${x:.2f}")


def get_total():
    total = 0
    while True:
        try:
            
            ask = input("What do you want to eat? ").title()
            
            if ask in menu:
                total += menu.get(ask)
                print("Total: $", end="")
                print ("{:.2f}".format(total))
            else:
                pass
        except EOFError:
            print()
            break

    return total

main ()
