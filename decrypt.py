from cryptography.fernet import Fernet
import os
import time

def decrypt_file():
    os.system('cls')

    with open('master.key', 'rb') as file:
        key = file.read()

    # path file to encrypt
    path = input("[ ~ ] Choose a file/folder to descrypt: ")

    fernet = Fernet(key)

    if os.path.isfile(path):
        # Read and encrypt file
        with open(path, 'rb') as file:
            decrypted = fernet.decrypt(file.read())

        # Save decrypted file
        with open(path, 'wb') as file:
            file.write(decrypted)

        file_name = os.path.basename(path)
        print(f"{file_name} decrypted successfully!")
    
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for filenames in files:
                file_path = os.path.join(root, filenames)
                with open(file_path, 'rb') as file:
                    decrypted = fernet.decrypt(file.read())
                with open(file_path, 'wb') as file:
                    file.write(decrypted)

                file_name = os.path.basename(file_path)
                print(f"{file_name} decrypted successfully!")

    time.sleep(1)
    os.system('cls')