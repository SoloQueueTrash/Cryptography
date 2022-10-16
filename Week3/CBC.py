from os import urandom 
from binascii import hexlify 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

key = urandom(16) 
iv = urandom(16) 

f = open("plaintext.txt", "r")
plaintext = f.read()

padder = padding.PKCS7(128).padder()
padded_data = padder.update(bytes(plaintext, encoding='utf-8')) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv)) 
encryptor = cipher.encryptor() # What happens if you don't pass 16−byte input? 
ct = encryptor.update(padded_data) + encryptor.finalize() 

print(hexlify(key))
print(hexlify(iv))

cphFile = open("ciphertext_encrypted.txt", "wb") 
cphFile.write(ct)