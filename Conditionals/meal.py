def main ():
    timing = input("What time is it my hungry friend?  ")
    hourn = convert(timing)
    print (hourn)

    
    if  hourn < 8.1 and hourn >= 7:
        print("breakfast time")
    elif hourn < 13.1 and hourn >= 12:
        print("lunch time")
    elif hourn < 19.1 and hourn >= 18:
        print("dinner time")
    



def convert (time):
    hours, minutes = time.split(":")
    hoursn = int(hours)
    minutesn = int(minutes) / 60
    newtime = hoursn + minutesn
    return float(newtime)




if __name__ == "__main__":
    main()
