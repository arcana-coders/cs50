def main ():
    plate = input("What do you want in your plate? ")
    
    cond1 = len(plate)
    cond4 = plate.isalnum()
    if not (2<= cond1 <=6 and cond4):
        print("Invalid")
        return
    
    cond2 = plate[0]
    cond3 = plate[1]
    if not (cond2.isalpha() and cond3.isalpha()):
        print("Invalid")
        return

    numbers = []
    for char in plate:
        if char.isdigit():
            numbers.append(char)

    if numbers:
        numstr = "".join(numbers)
        if numstr[0] == "0":
            print ("Invalid")
            return
        if not plate[-1].isdigit():
            print ("Invalid")
            return

        for i in range(1, len(plate) - 1):
            if plate[i].isalpha(): 
                if plate[i - 1].isdigit() and plate[i + 1].isdigit():
                    print("Invalid")
                    return

    print("Valid")
    
         



main ()