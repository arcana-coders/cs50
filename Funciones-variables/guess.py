def get_guess():
    guess = int(input("Pon un numero: "))
    return guess

def main ():
    guess = get_guess ()
    if guess == 50:
        print("Correctomundo!")
    else:
        print("casi pero no!!")


main ()


