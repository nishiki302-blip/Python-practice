def main():
    month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            date = input("Date: ")
            if '/' in date:
                m,d,y = date.split('/')
                m = int(m)
                d = int(d)
                y = int(y)
                if d > 31 or m > 12:
                    raise ValueError()
                print(f"{y:04}-{m:02}-{d:02}")
            elif ',' in date:
                md , y = date.split(',')
                m,d = md.split()
                d = int(d)
                y = int(y)
                if d > 31:
                    raise ValueError()
                print(f"{y}-{(month.index(m) + 1):02}-{d:02}")
            else:
                raise ValueError()
            
            break
        except ValueError:
            pass
main()