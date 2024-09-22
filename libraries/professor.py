import random

def main ():
    lp = get_level()
    op = generate_integer(lp)
    print (f""" 
           ==========================================
           NIVEL: {lp} 
           RESULTADO: {op} 
           ==========================================
           """)

def get_level ():
    levels = (1,2,3)
    while True:
        try:
            ask_user = int(input("Tell me the level you want: "))
            if not ask_user in levels:
                print("Just 1, 2 or 3 please")
                continue
            else:
                return (ask_user)
                
        except ValueError:
            print ("not a valid entry")
            continue

def generate_integer (level):
    usr_level = level

    values_lvl_1a = random.randrange(0,10)
    values_lvl_1b = random.randrange(0,10)
    values_lvl_2a = random.randrange(10,100)
    values_lvl_2b = random.randrange(10,100)
    values_lvl_3a = random.randrange(100,1000)
    values_lvl_3b = random.randrange(100,1000)
    if usr_level == 1:
        operation = operation_lvl()
        return(operation)


def operation_lvl():
    values_lvl_1a = random.randrange(0,10)
    values_lvl_1b = random.randrange(0,10)
    fail_counter = 0
    while True:

        usr_answer = input(f"{values_lvl_1a}+{values_lvl_1b}= ")
        secret_answer = (values_lvl_1a) + (values_lvl_1b)
        if fail_counter >= 2:
            print(f"La respuesta correcta es {secret_answer}")
            return(secret_answer)
        elif usr_answer.isalpha():
            print("Thats not even a number")
            fail_counter += 1
            # print (fail_counter)
            continue
        elif not usr_answer.isalpha():
            usr_answer_n = int(usr_answer)
            if usr_answer_n != secret_answer:
                print("EEE")
                fail_counter += 1
                # print(fail_counter)
                continue    
            else:        
                print(f"tu respuesta {usr_answer_n} es correcta")
                return(usr_answer_n)
            


if __name__ == "__main__":
    main ()
