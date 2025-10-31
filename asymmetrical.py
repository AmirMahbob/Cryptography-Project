from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class AsymmetricAlgorithms:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.private_key_pem = None
        self.public_key_pem = None

    def generate_rsa_keys(self, key_size=2048):
        key = RSA.generate(key_size)
        self.private_key = key.export_key()
        self.public_key = key.publickey().export_key()

    def rsa_encrypt(self, plaintext):
        rsa_key = RSA.import_key(self.public_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        ciphertext = cipher.encrypt(plaintext.encode())
        return ciphertext

    def generate_ecc_keys(self):
        self.private_key = ec.generate_private_key(ec.SECP256R1())
        self.public_key = self.private_key.public_key()

        self.private_key_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        self.public_key_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def ecc_encrypt(self, plaintext):
        public_key = serialization.load_pem_public_key(self.public_key_pem)
        shared_key = self.private_key.exchange(ec.ECDH(), public_key)
        
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=16,
            salt=None,
            info=b'handshake data'
        ).derive(shared_key)
        
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        
        padded_plaintext = plaintext.ljust((len(plaintext) + 15) // 16 * 16) 
        ciphertext = encryptor.update(padded_plaintext.encode()) + encryptor.finalize()
        
        return iv + ciphertext  