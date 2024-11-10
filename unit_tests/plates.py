def main():
    plate = input("What do you want in your plate? ")
    if is_valid (plate) == True:
        print("Valid")
    else:
        print("Invalid")

def is_valid (s):
    cond1 = len(s)
    cond4 = s.isalnum()
    if not (2<= cond1 <=6 and cond4):
        return False
        
    
    cond2 = s[0]
    cond3 = s[1]
    if not (cond2.isalpha() and cond3.isalpha()):
        return False
        

    numbers = []
    for char in s:
        if char.isdigit():
            numbers.append(char)

    if numbers:
        numstr = "".join(numbers)
        if numstr[0] == "0":
            return False
            
        if not s[-1].isdigit():
            return False
            

        for i in range(1, len(s) - 1):
            if s[i].isalpha(): 
                if s[i - 1].isdigit() and s[i + 1].isdigit():
                    return False
    return True
            
if __name__ == "__main__":
    main()
