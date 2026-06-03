"""
Prompt the user for a level,n.
If the user does not input 1 , 2 or 3, prompt again

Randomly generates 10 math problems formatted as 'X + Y =' wherein X and Y 
must be nonnegative integers.

Prompt the user to solve those problems.
If the answer is not correct, output 'EEE' and allowing the user three tries
If the answer is not correct after three tries, output the correct answer

Output the user's scores, the number of correct answers out of 10.
"""

import random

def main():
    level = get_level()
    total_correct_ans = 0
    check_list = ["a,b"]
    for _ in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        while f"{num1},{num2}" in check_list:
            num1 = generate_integer(level)
            num2 = generate_integer(level)
        
        check_list.append(f"{num1},{num2}")
        cal = num1 + num2
        count = 0
        while True:
            ans = int(input(f"{num1} + {num2} = "))
            if ans == cal:
                total_correct_ans += 1
                break
            print("EEE")
            
            count += 1
            if count == 3:
                print(f"{num1} + {num2} = {cal}")
                break
    print(f"Correct {total_correct_ans} out of 10 questions.")

def get_level():
    while True:
        try:    
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
            
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(1,10)
    elif level == 2:
        return random.randint(20,30)
    elif level == 3:
        return random.randint(40,50)
    else:
        raise ValueError("Invalid level.")

if __name__ == "__main__":
    main()