def main():
    goodbye = not_hello ()
    print (goodbye)

def not_hello ():
    some = input("tell me a number? ")
    if some.isdigit():
        return "its a number, i know, Bye"
    else:
        return "are you testing me? Bye"
    
if __name__ == "__main__":
    main()