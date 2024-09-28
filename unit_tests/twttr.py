def main ():
    tweet = input("Gimme your tweet, Ill do the work for you: ")
    print (shorten(tweet))

def shorten(word):
    vocals = {
        "a", "e", "i", "o", "u", 
        "A", "E", "I", "O", "U"
        }

    ttstrips = word.strip()
    #print (ttstrips)
    ttclean = []
    for letra in ttstrips:
        if letra not in vocals:
            ttclean.append(letra)
    ttj = "".join(ttclean)
    return ttj


if __name__ == "__main__":
    main()