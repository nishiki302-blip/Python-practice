# request user's grocery item until ctrl+z(eof)
# output user's grocery list in all uppercase
# sorted alphabetically by item
# prefixing each line with the number of times the user inputted that item
# no need to pluralize the items
# user's input case-insensitively

def main():
    note = {}
    while True:
        try:
            item = input("Item: ").upper()

        except EOFError:
            break
        
        else:
            if item in note:
                note[item] = note[item] + 1
            else:
                note[item] = 1
    print("")
    
    for name in sorted(note.keys()):
        print(f"{note[name]}  {name}")

main()