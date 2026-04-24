#Assume that user only input integers and 
#ignore any integer that isn’t an accepted denomination(25,10,5)
def main():
    price = 50

    while price != 0:
        print(f"Amount Due: {price}")
        charge = int(input("Insert Coin: "))
        if charge <= price:
            match charge:
                case 25:
                    price = price - charge
                case 10:
                    price = price - charge
                case 5:
                    price = price - charge
                case _:
                    continue

    print(f"Change Owed: {price}")

main()