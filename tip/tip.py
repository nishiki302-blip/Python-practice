def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #remove dollar sign , cast to float and round to 1
    return round(float(d.strip('$')),1)


def percent_to_float(p):
    #remove percentage sign , cast to float and divide 100
    return float(p.strip('%')) / 100


main()