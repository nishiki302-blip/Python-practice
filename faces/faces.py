#request for user input
say = input("Say: ")

def main():
    #use convert function and assign modify string to the new variable
    dsg_say = convert(say)
    #print modify string
    print(dsg_say)

#create convert function to change emoticons from user input
def convert(to):
    return to.replace(':)','🙂').replace(':(','🙁')

main()