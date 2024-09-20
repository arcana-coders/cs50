import random

def comput_think():
    while True:
        user_input = input("Please tell me a level: ")
        if user_input.isdigit() and int(user_input) > 0:
            user_input_1 = int(user_input)
            guess = random.randint(1, user_input_1)
            return guess
        else:
            print("Invalid input. Please enter a positive number.")
            continue

def usr_guess():
    guessing = comput_think()
    while True:
        usr_guess = input("now guess what number am I thinking: ")
        if usr_guess.isdigit():
            usr_guess = int(usr_guess)
            if usr_guess <= 0:
                print("Invalid input. Please enter a positive number.")
                continue
            if usr_guess < guessing:
                print("Too small!")
            elif usr_guess > guessing:
                print("Too large!")
            else:
                print("Just right!")
                return guessing
        else:
            print("Invalid input. Please enter a positive number.")

def main():
    usr_guess()

if __name__ == "__main__":
    main()