from main import menu, encrypt_file, decrypt_file

if __name__ == "__main__":
    while True:
        menu()
        try:
            option = int(input('> Choose a option: '))
        except ValueError:
            print("Please enter a valid number")
            continue

        match option:
            case 0:
                break
            case 1:
                encrypt_file()
            case 2:
                decrypt_file()
            case _:
                print('This option not exists')
