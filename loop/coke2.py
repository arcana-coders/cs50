def main ():
    cents = {25, 10, 5}
    coke = 50
    due = int(input(f"Amount Due: {coke}\n Insert Coin: "))
    if due in cents:
        while due < 50:
        # amount = coke - due    
            due += int(input(f"Amount Due: {coke - due}\n Insert Coin: "))

        print(f"Change Owed: {due - 50}")
    elif due != cents:
        due += int(input(f"Amount Due: {coke}\n Insert Coin: "))     

main ()