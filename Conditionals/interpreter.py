def main ():
    math = input("Write a math question  ")
    if "+" in math:
        plus = math.split("+")
        sum1 = int(plus[0])
        sum2 = int(plus[1])
        plusresult = sum1 + sum2
        print(float(plusresult))
    elif "-" in math:
        minus = math.split("-")
        less1 = int(minus[0])
        less2 = int(minus[1])
        lessresult = less1 - less2
        print(float(lessresult))
    elif "*" in math:
        por = math.split("*")
        por1 = int(por[0])
        por2 = int(por[1])
        porresult = por1 * por2
        print(float(porresult))
    elif "/" in math:
        entre = math.split("/")
        entre1 = int(entre[0])
        entre2 = int(entre[1])
        entreresult = entre1 / entre2
        print(float(entreresult))
    else:
        print("something is wrong")
    
    

    #print(f"The answer is {plusresult}")



main ()
