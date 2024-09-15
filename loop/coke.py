def main():
    cents = {25, 10, 5} 
    coke = 50  
    due = 0 

    while due < coke:
        coin = int(input(f"Amount Due: {coke - due}\n Insert Coin: "))
    
        if coin in cents:
            due += coin  
    
    change = due - coke
    print(f"Change Owed: {change}")

main()
