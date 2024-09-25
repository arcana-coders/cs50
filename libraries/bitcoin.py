import requests
import json
import sys

def main ():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too much arguments")
    elif len(sys.argv) == 2:
        money_usr = sys.argv[1]
        if money_usr.isalpha():
            sys.exit("Thats not a number")
        money_fl = float(money_usr)
        if type(money_fl) == float:
            print(f"Sir, yo have this {money_fl} bitcoins")
        else:
            print(f"you are giving this {money_usr}") 

def get_bitcoin():
    price_btc = requests.get ("https://api.coindesk.com/v1/bpi/currentprice.json")
    print    


if __name__ == "__main__":
    main()