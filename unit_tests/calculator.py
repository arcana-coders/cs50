def main ():
    # print("hola mundo")
    calc = int(input("what do you want to calc? "))
    
    print(f"your square is {square(calc)}")

def square (n):
    return n ** 2
    

if __name__ == "__main__":
    main()