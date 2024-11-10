import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print ("too few arguments")
        sys.exit(1)
    elif len(sys.argv) >= 3:
        print("a lot of arguments")
        sys.exit(1)
    elif len(sys.argv) == 2 and not sys.argv[1].endswith("csv"):
        print("this is not a csv file and you know it")
        sys.exit(1)

    filename = sys.argv[1]
    tabcsv = cutecsv (filename)
    print(tabcsv)
    
def cutecsv (filename):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                data.append(row)
        return tabulate(data, headers="firstrow", tablefmt="grid")
    except FileNotFoundError:
        print("file doesnt exist")
        sys.exit(1)

if __name__ == "__main__":
    main()