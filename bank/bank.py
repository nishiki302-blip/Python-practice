#Greeting by bank manager
greet = input("Greeting: ")

#Remove whitespace and make case-insensitive to greet sentence
greet = greet.strip().casefold() 

#check if the greet sentence meet 'hello', fine $0
if greet.startswith("hello") :
    print("$0")

#starts with 'h' but not 'hello', fine $20
elif greet.startswith("h"):
    print("$20")

#otherwise, fine $100
else: 
    print("$100")