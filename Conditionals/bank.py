def main():
    greet = input("Greeting and win money!! ")
    if greet.__contains__("Hello"):
        print("$0")
    elif greet.startswith("H") and greet != "Hello":
        print("$20")
    else:
        print("$100")
        
main()