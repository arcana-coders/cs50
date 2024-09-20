from pyfiglet import Figlet
import sys
from random import choice


def main():

    figlet = Figlet()

    fonts_list = figlet.getFonts()
    fonts_random = choice(fonts_list)
    figlet.setFont(font=fonts_random)
    if len(sys.argv) == 1:
        txt_fig = input("Please tell me what you want in figlet: ")
        print(figlet.renderText(txt_fig))
    elif len(sys.argv) == 3 and sys.argv[2] not in fonts_list:
        sys.exit("The font dont exist")
    elif len(sys.argv) == 3 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("The parameter is invalid")

    elif len(sys.argv) == 3 and sys.argv[2] in fonts_list:
        txt_fig = input("Please tell me what you want in figlet: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(txt_fig))
    else:
        sys.exit("I dont know what happen here, sorry my friend.")


if __name__ == "__main__":
    main()
