import re

def main():
    print(count(input("Text: ")))

def count(s):
    allums = r'\bum\b[.,?!]*'
    ums = re.findall(allums, s, re.IGNORECASE)  
    hmums = len(ums)
    return hmums

if __name__ == "__main__":
    main()
