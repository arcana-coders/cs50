import random

def comput_think():
    while True:
        user_input = input("Please tell me a level: ")
        if user_input.isdigit() and int(user_input) != 0:
            user_input_1 = int(user_input)
            guess = (random.randint(1,user_input_1))
            # print(guess)
            return guess
                
        else:
            continue

def usr_guess():
    guessing = comput_think()
    while True:
        
        usr_guess = input("now guess what number am i thinking: ")
        if usr_guess.isdigit() and int(usr_guess) != 0:
                if int(usr_guess) < guessing:
                    print("Too small")
                    continue
                elif int(usr_guess) > guessing:
                    print("Too large!")
                    continue
                elif usr_guess == guessing:
                    return(guessing)    
        return(guessing)            
                    
        
                    


def main ():
    right = usr_guess()
    # number = comput_think()
    print (f"just right, the number {right} is damn correct!")
    
    



main ()