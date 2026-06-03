"""
Prompt the user for names,one per line,until the user input Ctrl + Z
Assume that the user will input at least one name
Bid adieu to those names,separating two names with one 'and',three names
with two ',' and one 'and',n names with n-1 comma and one 'and'

"""

import inflect


def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ")

        except EOFError:
            break

        else:
            names.append(name)

    print(f"Adieu, adieu, to {p.join(names)}")


main()
