distances = {
    "Votager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44

}

def main ():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")
#    for name in distances.keys():
#        print(f"{name} is {distances[name]} Au from Earth")


def convert(au):
    return au * 149597870700



main ()