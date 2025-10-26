from cryptography.fernet import Fernet
import os
import time
from tqdm import tqdm

def encrypt_file():
    os.system('cls')

    # Generate key only if it does not exist
    if not os.path.exists('master.key'):
        key = Fernet.generate_key()

        with open('master.key', 'wb') as file:
            file.write(key)
    else:
        with open('master.key', 'rb') as file:
            key = file.read()

    # path file to encrypt
    path = input("[ ~ ] Choose a file/folder to encrypt: ")

    fernet = Fernet(key)

    if os.path.isfile(path):
        # Read and encrypt file
        with open(path, 'rb') as file:
            encrypted = fernet.encrypt(file.read())

        # Save encrypted file
        with open(path, 'wb') as file:
            file.write(encrypted)

        print("File encrypted successfully!")
    
    elif os.path.isdir(path):
        # Pegar todos os arquivos da pasta e subpastas
        all_files = []
        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename == 'master.key':
                    continue
                all_files.append(os.path.join(root, filename))
        
        total = len(all_files)
        for file_path in tqdm(all_files, desc="Encrypting files", unit="file"):
            with open(file_path, 'rb') as file:
                encrypted = fernet.encrypt(file.read())
            with open(file_path, 'wb') as file:
                file.write(encrypted)
            
        print("\nFolder encrypted successfully!")

    time.sleep(0.5)
    os.system('cls')