say = input("Say: ")

def main():
    dsg_say = convert(say)
    print(dsg_say)

def convert(to):
    return to.replace(':)','🙂').replace(':(','🙁')

main()