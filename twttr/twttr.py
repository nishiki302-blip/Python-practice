def main():
    name = input("Input: ")
    name = short(name)
    print(name)

def short(word):
    n_list = []
    vowel = ['a','e','i','o','u']
    for n in word:
        if n.lower() in vowel:
            continue
        n_list.append(n)
    return "".join(n_list)

main()