from cryptography.fernet import Fernet

def generate_key(file_path = 'encryption_key.key'):
    key = Fernet.generate_key()
    with open (file_path, 'wb') as key_file:
        key_file.write(key)
        print (f"Encryption key is saved in to: {file_path}")

generate_key()


def load_key(file_path = 'encryption_key.key'):
    with open (file_path, 'rb') as key_file:
        key = key_file.read
        return key
    
load_key()

def encrypt_file (input_file, output_file, key):
    fernet = Fernet(key)
    with open('input_file', 'rb') as file:
       original =  file.read()
       encrypted = fernet.encrypt(original)
    
    with open(output_file, 'wb') as file:
        file.write(encrypted)
        print(f"File encrypted and saved to: {output_file}")


