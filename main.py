from cryptography.fernet import Fernet

# Generate and save an encryption key to a file
def generate_key(file_path = 'encryption_key.key'):
    key = Fernet.generate_key() # Generates a random 32 bit key
    with open (file_path, 'wb') as key_file:
        key_file.write(key)
        print (f"Encryption key is saved in to: {file_path}")

# Load an existing key from a file
def load_key(file_path = 'encryption_key.key'):
    with open (file_path, 'rb') as key_file:
        key = key_file.read()
        return key
    

# Encrypt the file and save the output to a new file
def encrypt_file (input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
       original =  file.read()
       encrypted = fernet.encrypt(original)
    
    with open(output_file, 'wb') as file:
        file.write(encrypted)
        print(f"File {input_file} encrypted and saved to: {output_file}")

# Decrypt the file and save the output to a new file
def decrypt_file (input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted = file.read() 
        decrypted = fernet.decrypt(encrypted) 
    
    with open(output_file, 'wb') as file:
        file.write(decrypted)
        print(f"File {input_file} decrypted and saved to: {output_file}")

# Adding user interface
def main():
    print("Welcome to the Encryption/Decryption Tool")
    while True:
        print("1. Generate an Encryption key")
        print("2. Encrypt a file")
        print("3. Decrypt a file")
        print("4. Exit the program")
        option = input ("Please choose an option: ")
        
        # The user is given the choice to select a key path or go with default
        if option   == '1':
            file_path = input ("Enter the file path to save the key (default: 'encryption_key.key'): ") or 'encryption_key.key'
            generate_key(file_path)

        # Encryption option
        elif option == '2':
            input_file = input("Enter the path of the file to encrypt: ")
            output_file = input("Enter the name of the output file: ")
            key_path = input ("Enter the path of the encryption key otherwise the default will be used") or 'encryption_key.key'
            try:
                key = load_key(key_path)
                encrypt_file(input_file, output_file, key)

             # handling errors in a professional manner
            except Exception as e:
                print(f"Error during encryption: {e}")
        # Decryption option
        elif option == '3':
            input_file = input("Enter the path of the file to decrypt: ")
            output_file = input("Enter the name of the output file: ")
            key_path = input ("Enter the path of the dncryption key otherwise the default will be used: ") or 'encryption_key.key'
            try:
                key = load_key(key_path)
                decrypt_file(input_file, output_file, key)

            # handling errors in a professional manner
            except Exception as e:
                print(f"Error during decryption: {e}")

        # Exiting the program
        elif option == '4':
            print("Exiting the program")
            break
        else:
            print("Please choose a valid option")


main()


       

        


