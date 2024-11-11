import sys
import csv

def main():
    
    if len(sys.argv) < 3:
        print("Too few arguments")
        sys.exit(1)
    elif len(sys.argv) > 4:
        print("Too many arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        print("Both files should be CSV files")
        sys.exit(1)

    filebefore = sys.argv[1]
    fileafter = sys.argv[2]
    process_csv(filebefore, fileafter)

def process_csv(filebefore, fileafter):
    try:
        with open(filebefore, "r") as infile:
            reader = csv.DictReader(infile)
            fieldnames = ["first", "last", "house"]

            with open(fileafter, "w", newline="") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()  
                for row in reader:
                    last, first = row["name"].split(", ")
                    new_row = {
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    }
                    writer.writerow(new_row)  

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

if __name__ == "__main__":
    main()