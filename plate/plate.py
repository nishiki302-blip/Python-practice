#max characters -> 6, min characters -> 2
#characters must start with at least 2 letters and end with numbers
#first number cannot be a zero
#no periods, spaces and punctuation marks are allowed
#Assume user's input is uppercase character

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_length(s) and check_start_end(s) and check_start_num(s) and check_name(s):
        return True
    else: 
        return False

def check_length(s):
    return len(s) >=2 and len(s) <= 6
    
def check_start_end(s):
    return s[0:2].isalpha() and s[-1].isdigit()

def check_start_num(s):
    for i in s:
        if i.isnumeric():
            return i != '0'

def check_name(s):
    return s.isidentifier()

        

main()