def main():
    life = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    clean = life.replace(" ", "").lower()

    match clean:
        case "42" | "fortytwo" | "forty-two":
            print("Yes")
        case _:
            print("No")

main()