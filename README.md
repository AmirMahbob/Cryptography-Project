# Cryptography Project 🔐

A comprehensive and practical cryptography project with a graphical user interface (GUI) that implements **symmetric, asymmetric, and hashing algorithms**.  
This project is ideal for learning cryptography concepts and having a handy tool for encrypting text.

---

## Features

### 🔹 Symmetric Encryption
- AES (128-bit)
- DES
- 3DES
- CBC mode for enhanced security
- Randomly generated **key and IV** for each encryption
- Output includes **key, IV, and ciphertext**

### 🔹 Asymmetric Encryption
- **RSA (2048-bit)**
  - Generates private and public keys
  - Secure encryption using PKCS1_OAEP
- **ECC (SECP256R1)**
  - Encrypts text with ECDH and AES-CBC
  - Derives secure shared key using HKDF
- Output includes **public key and ciphertext**

### 🔹 Hashing
- SHA-256
- SHA3-256
- MD5
- Produces hexadecimal hash of input text

### 🔹 Graphical User Interface (GUI)
- Beautiful and simple GUI using Tkinter
- Clear input forms and readable output
- Result window with **copy and save functionality**
- Easy navigation back to main menu

---

## Project Screenshots
<p align="center">
  <img src="https://github.com/AmirMahbob/Cryptography-Project/blob/main/picture.png?raw=true" alt="Cryptography GUI" width="400"/>
</p>

---

## Example Usage

### Symmetric Encryption (AES)
```text
Input: Hello World
Key: 3a1f5b6c7d8e9f01a2b3c4d5e6f7g8h9
IV: 1f2e3d4c5b6a7980a1b2c3d4e5f6g7h8
Ciphertext: aabbccddeeff00112233445566778899
```
### Asymmetric Encryption (RSA)
```
Input: Hello World
Public key:
3082010a0282010100aabbccddeeff...
Ciphertext: 11223344556677889900aabbccddeeff
```
### Hashing (SHA-256)
```
Input: Hello World
Hash: a591a6d40bf420404a011733cfb7b190d62c65bf0abc5e7b6c02aaad77d09c
```

---

### Installation & Running
1. Clone the repository:
   ```
   git clone https://github.com/username/cryptography-project.git
   cd cryptography-project
   ```

2. Install required libraries:

    a. Install on Windows:
     ```
      pip install pycryptodome
      pip install cryptography
      python -m pip install tk
     ```
    b. Install on Mac:
     ```
      brew install python-tk  
      pip3 install pycryptodome
      pip3 install cryptography
     ```
   c. Install on Linux:
     ```
      sudo apt update
      sudo apt install python3-tk
      pip3 install pycryptodome
      pip3 install cryptography
     ```
4. Run the GUI:
   ```
   python gui.py
   ```

---

Project Structure
```
cryptography-project/
│
├─ gui.py               # Graphical User Interface
├─ symmetrical.py       # Symmetric algorithms (AES, DES, 3DES)
├─ asymmetrical.py      # Asymmetric algorithms (RSA, ECC)
├─ hash.py              # Hashing algorithms (SHA-256, SHA3-256, MD5)
├─ requirements.txt     # Required Python packages
└─ README.md            # Project documentation
```
