import random

def main():
    while True:
        user_input = input("Please tell me a level: ")
        if user_input.isdigit() and int(user_input) != 0:
            user_input_1 = int(user_input) + 1
            guess = (random.randint(1,user_input_1))
            usr_guess = input("now guess what number am i thinking: ")
            if usr_guess.isdigit() and int(usr_guess) != 0:
                if int(usr_guess) < guess:
                    print("Too small")
                    continue
                elif int(usr_guess) > guess:
                    print("Too large!")
                    continue
                elif usr_guess == guess:
                    print("Just right!")
                    break

            break
        else:
            continue








main ()