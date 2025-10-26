from encrypt import encrypt_file
from decrypt import decrypt_file
import os

os.system('cls')

def menu():
    print('=-=-=-=-=-=-=-=-=-=-=')
    print('=  FILE ENCRYPTION  =')
    print('=-=-=-=-=-=-=-=-=-=-=')
    print('1. Encrypt File')
    print('2. Decrypt File')
    print('0. Exit')
    print('=-=-=-=-=-=-=-=-=-=-=')
    print(' ')


while True:
    menu()
    option = int(input('> Choose a option: '))
    
    match option:
        case 0:
            break
        case 1:
            encrypt_file()
        case 2:
            decrypt_file()
        case _:
            print('This option not exists')