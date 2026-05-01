def main():
    while True:
        fuel = input("Fraction: ")
        try:
            print(show_fuel_percent(fuel))

        except (ValueError,ZeroDivisionError):
            pass

        else:
            break

def show_fuel_percent(fraction):
    x , y = fraction.split('/')
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError()
    elif x > y or x < 0 or y < 0:
        raise ValueError()
    result = round((x/y) * 100)
    if result <= 1:
        return "E" 
    elif result >= 99:
        return "F"
    else:
        return f"{result}%"

main()