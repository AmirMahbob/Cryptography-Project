import hashlib

class Hashing:
    def __init__(self):
        pass

    def sha256(self, data):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode())
        return sha256_hash.hexdigest()

    def sha3_256(self, data):
        sha3_256_hash = hashlib.sha3_256()
        sha3_256_hash.update(data.encode())
        return sha3_256_hash.hexdigest()

    def md5(self, data):
        md5_hash = hashlib.md5()
        md5_hash.update(data.encode())
        return md5_hash.hexdigest()