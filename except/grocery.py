

def main():
    list = {}
    while True:
        try:
            super = input("").upper()
            if super in list:
                 list[super]+= 1
            else:
                 list[super] = 1
        
        except EOFError:
                #print()
                #break
            print()
            for item in sorted(list):
                print(f"{list[item]} {item}")
            
            break
    return

main ()