def main():
    while True:
        fraction = input("How much gas is on the gauge? ")
        try:
            x,y = fraction.split("/")
            if x.isalpha() or y.isalpha():
                continue
            elif x > y:
                continue
            elif y == 0:
                continue 
            else:
                fraction = "/".join([str(x), str(y)])
                percentage = convert(fraction)
                gauge(percentage)
                break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)    
    percentege = (int(x) / int(y)) * 100
    percentege = int(percentege)
    # print (percentege)
    return percentege

def gauge(percentage):
    if percentage <= 1:
        print("E")
        return ("E")
    if percentage >= 99:
        print("F")
        return ("F")
    else:
        print(f"{percentage}%")
        return f"{percentage}%"
    


if __name__ == "__main__":
    main()
