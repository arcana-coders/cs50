import re

def main():
    ip = input("IPv4 Address: ")
    answer = validate(ip)
    print(answer)

def validate(ip):
    ipv4 = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(ipv4, ip)
    
    if match:
        numeros = []
        for i in range(1, 5):
            numero = int(match.group(i))
            numeros.append(numero)
        
        for numero in numeros:
            if numero < 0 or numero > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
