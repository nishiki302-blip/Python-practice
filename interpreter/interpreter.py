expr = input("Expression: ")
x , y , z = expr.split(" ")
x = int(x)
z = int(z)

def main():
    print(calculate(x,y,z))

def calculate(int1,operator,int2):
    match operator:
        case "+":
            result = float(int1 + int2)
            return f"{result:.1f}"
        
        case "-":
            result = float(int1 - int2)
            return f"{result:.1f}"
        
        case "*":
            result = float(int1 * int2)
            return f"{result:.1f}" 
        
        case "/":
            result = float(int1 / int2)
            return  f"{result:.1f}"
        
        case _:
            return "Please check your expression again"
        
main()