def main ():
    greet = input("Greeting and win money!! ")
    print (value(greet))
    

def value(greeting):
    if greeting.__contains__("Hello"):
        return("$0")
    elif greeting.startswith("H") and greeting != "Hello":
        return("$20")
    else:
        return("$100")




if __name__ == "__main__":
    main()