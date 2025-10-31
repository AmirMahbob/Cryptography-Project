from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad
import os

class SymmetricAlgorithms:
    def __init__(self):
        self.key = None
        self.iv = None

    def generate_key(self, algorithm):
        if algorithm == 'AES':
            self.key = os.urandom(16)  
            self.iv = os.urandom(16) 
        elif algorithm == 'DES':
            self.key = os.urandom(8)  
            self.iv = os.urandom(8)  
        elif algorithm == '3DES':
            self.key = DES3.adjust_key_parity(os.urandom(24))  
            self.iv = os.urandom(8)  
        else:
            raise ValueError("Invalid algorithm name!")

    def encrypt(self, plaintext, algorithm):
        self.generate_key(algorithm)
        if algorithm == 'AES':
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        elif algorithm == 'DES':
            cipher = DES.new(self.key, DES.MODE_CBC, self.iv)
        elif algorithm == '3DES':
            cipher = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        else:
            raise ValueError("Invalid algorithm name!")

        padded_data = pad(plaintext.encode(), cipher.block_size)
        return cipher.encrypt(padded_data)