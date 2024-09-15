def main():
    entrada = input("Enter something: ")

    # Condiciones a verificar
    if not (2 <= len(entrada) <= 6):
        print("Invalid - Must be between 2 and 6 characters.")
        return

    if not (entrada[0].isalpha() and entrada[1].isalpha()):
        print("Invalid - First two characters must be letters.")
        return

    if not entrada.isalnum():
        print("Invalid - Only letters and numbers are allowed.")
        return

    numeros = [char for char in entrada if char.isdigit()]

    if numeros:
        num_str = "".join(numeros)

        # Verificar si el primer número es 0
        if num_str[0] == "0":
            print("Invalid - Numbers cannot start with zero.")
            return

        # Verificar si la cadena termina en un número
        if not entrada[-1].isdigit():
            print("Invalid - If there are numbers, the string must end with a number.")
            return

        # Verificar si los números están agrupados
        if any(char.isalpha() and entrada[i - 1].isdigit() and entrada[i + 1].isdigit() for i, char in enumerate(entrada) if 0 < i < len(entrada) - 1):
            print("Invalid - Numbers must be grouped.")
            return

    print("Valid")

main()
