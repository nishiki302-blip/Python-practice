"""
Expects zero or two command-line arguments:

Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case 
the first of the two should be -f or --font, and the second of the two 
should be the name of the font.
Provide an error message if the name of the font is not a valid name.

Prompts the user for a str of text.
Outputs that text in the desired font.

"""
from pyfiglet import Figlet
import sys

def main():
    figlet = Figlet()
    if len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            if sys.argv[2] not in figlet.getFonts():
                sys.exit('Invalid usage.')
            figlet.setFont(font=sys.argv[2])
            
        else:
            sys.exit('Invalid usage.')
    
    str = input("Input: ")
    print(figlet.renderText(str))

main()