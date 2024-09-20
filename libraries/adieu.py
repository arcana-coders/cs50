import inflect
p = inflect.engine()

def main ():
    names = []
    try:
        while True:
    
            name_list = input("Please tell me the names: ")
            names.append(name_list)
            
    except EOFError:
        pass
    print (f"Adieu, adieu, to {p.join(names)}")

    


main ()

