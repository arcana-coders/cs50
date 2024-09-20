import emoji

def main ():
    normal = input("Please gimme what you want in emoji: ")
    print (emoji.emojize(f'Output: {normal}', language='alias'))


main ()