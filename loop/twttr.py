def main ():
    vocals = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    tweet = input("Gimme your tweet, Ill do the work for you: ")
    ttstrips = tweet.strip()
    #print (ttstrips)
    ttclean = []
    for letra in ttstrips:
        if letra not in vocals:
            ttclean.append(letra)

    #        print (ttclean)
    ttj = "".join(ttclean)
    print (ttj)


main ()
