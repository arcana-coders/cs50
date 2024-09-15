def main ():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Whatś n? "))
        if n > 0:
            break
    return n
    
def meow(n):
    for _ in range(n):
        print ("meow")

main ()

# imprimira n veces 
#while True:
#    n = int(input("Whatś n? "))
#    if n > 0:
#        break

#for _ in range(n):
#    print ("meow")

# se usa slash n para cambiar renglon, y el end y nada entre comillas para que no deje espacio
# print ("meow\n" * 3, end="")

# usando range y guion bajo como variable
#for _ in range(3):
#    print ("meow")

# usando list

#for i in [0, 1, 2]:
#    print ("meow")

# usando While
#i = 0
#while i < 3:
#    print ("meow")
#    i = i + 1
    # same that i += 1
 