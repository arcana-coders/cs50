import sys

def main ():
    if len(sys.argv) < 2:
        print("too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) >= 3:
        print("too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) == 2 and not sys.argv[1].endswith("py"):
        print("Not a python file")
        sys.exit(1)


    filename = sys.argv[1]
    count = lines(filename)
    print (count)

def lines (filename):
    count_lines = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                nospace_line = line.lstrip()
                if nospace_line:
                    if not nospace_line.startswith("#"):
                        count_lines += 1

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    return count_lines



if __name__ == "__main__":
    main()