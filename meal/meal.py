def main():
    #Assume user's input is 24-hour time format h:mm (or) hh:mm
    #and 12-hour format h:mm a.m. (or) hh:mm p.m.
    time = input("Time: ").strip()
    
    #to handle 12-hour time format
    if time.endswith("."):
        time , period = time.split(" ")
        time = convert(time,period)

    #to handle 24-hour time format
    else:
        time = convert(time)

    if (7.00 <= time <= 8.00):
        print("Breakfast time")

    elif (12.00 <= time <= 13.00):
        print("Lunch time")

    elif (18.00 <= time <= 19.00):
        print("Dinner time")

    else: 
        return

def convert(t = 00.00,am_pm = None):
    #Split user's input with ':' and store in hours and minutes variable
    hours , minutes = t.split(":")

    h1 = float(hours)

    # 1 hour = 60 minutes
    h2 = float(float(minutes) / 60.0)
    h = h1 + h2

    if am_pm == "p.m." and (1.00 <= h < 12.00):
        add_12 = h + 12
        return add_12
    
    elif am_pm == "a.m." and (12.00 <= h < 13.00):
        return 00.00

    else:
        return h


    

main()