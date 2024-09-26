import requests
import json
import sys

def main ():
    try:
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
                btc_price = get_bitcoin()
                money_btc = money_fl * btc_price
                print(f"${money_btc:,.4f}")
            else:
                print(f"you are giving this {money_usr}") 
    except requests.RequestException:
        sys.exit("Not connection")

def get_bitcoin():
    price_btc = requests.get ("https://api.coindesk.com/v1/bpi/currentprice.json")
    btc_js = price_btc.json()
    
    btc_qu = btc_js ["bpi"]["USD"]["rate_float"]
    return btc_qu
                    


if __name__ == "__main__":
    main()