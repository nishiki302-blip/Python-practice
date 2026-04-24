def main():
    name = input("Camel case: ")
    print(convert_snake_case(name))

def convert_snake_case(word):
    n_list = []
    for n in word:
        if n.isupper():
            n_list.append(f"_{n.lower()}")
        else:
            n_list.append(n)

    word = "".join(n_list)
    return f"Snake case: {word}"

main()