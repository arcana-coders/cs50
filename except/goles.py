def main ():
    goles = {}

    while True:
        try:
            anota = input("Nombre del anotador: ").capitalize()
            if anota in goles:
                goles[anota]+= 1
            else:
                goles[anota] = 1

        except EOFError:
            print()
            for gol in goles:
                print(f"El jugador {gol} tiene {goles[gol]} goles anotados")
            break
    return

main ()
