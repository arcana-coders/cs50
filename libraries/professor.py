import random

def main ():
    lp = get_level()
    grade = generate_integer(lp)
    
    print (f""" 
           ==========================================
           NIVEL: {lp} 
           CALIFICACION: {grade} 
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
    if usr_level == 1:
        counter = 0
        grade = 0
        while counter != 10:
            success = operation_lvl_1()
            grade += success
            counter += 1
            print (f"llevamos {counter} operaciones y {grade} de calificacion")
            continue    
        return grade
    elif usr_level == 2:
        counter = 0
        grade = 0
        while counter != 10:
            success = operation_lvl_2()
            grade += success
            counter += 1
            print (f"llevamos {counter} operaciones y {grade} de calificacion")
            continue    
        return grade
    elif usr_level == 3:
        counter = 0
        grade = 0
        while counter != 10:
            success = operation_lvl_3()
            grade += success
            counter += 1
            print (f"llevamos {counter} operaciones y {grade} de calificacion")
            continue    
        return grade


def operation_lvl_1():
    values_lvl_1a = random.randrange(0,10)
    values_lvl_1b = random.randrange(0,10)
    fail_counter = 0
    secret_answer_count = 0
    success_counter = 0
    while True:

        usr_answer = input(f"{values_lvl_1a} + {values_lvl_1b} = ")
        secret_answer = (values_lvl_1a) + (values_lvl_1b)
        secret_answer_count += 1
        if fail_counter == 2:
            usr_answer_n = int(usr_answer)
            if usr_answer_n == secret_answer:
                success_counter += 1
                print(f"tu respuesta {usr_answer_n} es correcta")
                break
            else:
                print(f"La respuesta correcta es {secret_answer}")
                break        
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
                success_counter += 1
                break
    return success_counter                
            
def operation_lvl_2():
    values_lvl_2a = random.randrange(10,100)
    values_lvl_2b = random.randrange(10,100)
    fail_counter = 0
    secret_answer_count = 0
    success_counter = 0
    while True:

        usr_answer = input(f"{values_lvl_2a} + {values_lvl_2b} = ")
        secret_answer = (values_lvl_2a) + (values_lvl_2b)
        secret_answer_count += 1
        if fail_counter == 2:
            usr_answer_n = int(usr_answer)
            if usr_answer_n == secret_answer:
                success_counter += 1
                print(f"tu respuesta {usr_answer_n} es correcta")
                break
            else:
                print(f"La respuesta correcta es {secret_answer}")
                break
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
                success_counter += 1
                break
    return success_counter    

def operation_lvl_3():
    values_lvl_3a = random.randrange(100,1000)
    values_lvl_3b = random.randrange(100,1000)
    fail_counter = 0
    secret_answer_count = 0
    success_counter = 0
    while True:

        usr_answer = input(f"{values_lvl_3a} + {values_lvl_3b} = ")
        secret_answer = (values_lvl_3a) + (values_lvl_3b)
        secret_answer_count += 1
        if fail_counter == 2:
            usr_answer_n = int(usr_answer)
            if usr_answer_n == secret_answer:
                success_counter += 1
                print(f"tu respuesta {usr_answer_n} es correcta")
                break
            else:
                print(f"La respuesta correcta es {secret_answer}")
                break
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
                success_counter += 1
                break
    return success_counter              


if __name__ == "__main__":
    main ()
