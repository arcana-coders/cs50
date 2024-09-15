def main():
    meses = ["adjust", "january", "february", "march", "april",
             "may", "june", "july", "august",
              "september", "october",
             "november", "december"
    ]
    while True:
        try:
            weird_date = input("Date: ")
            weird_date = weird_date.replace(" ","/")
            weird_date = weird_date.replace(",","")
            # print(weird_date)
            mm, dd, yyyy = weird_date.split("/")
            # print(f"{mm},{dd},{yyyy}")

            if mm.isdigit():
                # print("is digit")
                if not int(mm) in range(1,13):
                    # print("not month")    
                    continue
            else:
                mm = mm.lower()
                if mm not in meses:
                    # print(f"{mm} no esta en la lista")
                    continue
                elif mm in meses:
                    mm = meses.index(mm)
            if not int(dd) in range(1,32):
                # print("not day")
                continue
            if not int(yyyy) in range(2025):
                # print("not year")
                continue
            
            
            else:
                yyyy = int(yyyy)
                mm = int(mm)
                dd = int(dd)
                print (f"{yyyy}-{mm:02}-{dd:02}")
                break


        except ValueError:
            # print(ValueError)
            pass
    
            


main ()