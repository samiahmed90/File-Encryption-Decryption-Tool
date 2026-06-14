from cryptography.fernet import Fernet

def generate_key(file_path = 'encryption_key.key'):
    key = Fernet.generate_key()
    with open (file_path, 'wb') as key_file:
        key_file.write(key)
        print (f"Encryption key is saved in to {file_path}")

generate_key()