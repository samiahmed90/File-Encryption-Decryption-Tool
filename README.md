# File Encryption Decryption Tool

A command-line tool built in Python that allows users to securely encrypt and decrypt files using symmetric key encryption (Fernet/AES-128).

## Features
- Generate a secure encryption key
- Encrypt any file on your computer
- Decrypt encrypted files
- Save keys and files to any location on your computer

## Technologies Used
- Python 3
- `cryptography` library (Fernet)

## How to Use

### 1. Install dependencies
pip install cryptography

### 2. Run the program
python main.py

### 3. Choose an option
1. Generate an Encryption key
2. Encrypt a file
3. Decrypt a file
4. Exit the program

## Important Notes
- Keep your encryption key safe — if you lose it, you cannot decrypt your files
- Use the same key to decrypt that you used to encrypt
- The program supports any file type (.txt, .pdf, .png, etc.)

## Author
samiahmed90