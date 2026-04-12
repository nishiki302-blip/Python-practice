def main():
    file = input("File Name: ")
    _ , y = file.split('.')
    file = file.strip().casefold()

    if file.endswith(('.gif','.jpg','png','jpeg')):
        print(f"image/{y}")

    elif file.endswith('.pdf'):
        print("application/pdf")

    elif file.endswith('.txt'):
        print(f"text/{y}")

    elif file.endswith('.zip'):
        print(f"archive/{y}")

    else:
        print("application/octet-stream")


main()