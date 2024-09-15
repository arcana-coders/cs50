def main ():
    x = get_fuel()
    if x >= 99:
        print("F")
    elif x <= 1:
        print("E")
    else:
        print(f"{x}%")

def get_fuel():

    while True:
        try:
            fuel = input("How much gas is on the gauge? ")
            uno , dos = fuel.split("/")
            uno = int(uno)
            dos = int(dos)
            answer = (uno / dos) * 100
            answer = round(answer)
            if answer > 100:
                pass
            elif answer < 0:
                pass
            else:
                return int(answer)

        except (ValueError, ZeroDivisionError):
            pass



main ()