# Adaptado de https://nitratine.net/blog/post/python-gcm-encryption-tutorial/

from Cryptodome.Cipher import AES
from os import urandom
from binascii import hexlify

BUFFER_SIZE = 1024 * 1024

# Open files
file_in = open("plaintext.txt", 'rb') 
file_out = open("encrypted_aesgcm.txt", 'wb')

key = urandom(16)  
key_file = open("key.txt", "wb")
key_file.write(key)

cipher = AES.new(key, AES.MODE_GCM)

iv_file = open("iv.txt", "wb")
iv_file.write(cipher.nonce)

# Read, encrypt and write the data
data = file_in.read(BUFFER_SIZE)  # Read in some of the file
while len(data) != 0:
    encrypted_data = cipher.encrypt(data)  # Encrypt the data we read
    file_out.write(encrypted_data)  # Write the encrypted data to the output file
    data = file_in.read(BUFFER_SIZE)  # Read some more of the file to see if there is any more left

tag = cipher.digest()  

tag_file = open("tag.txt", "wb")
tag_file.write(tag)

file_in.close()
tag_file.close()
iv_file.close()
key_file.close()
file_out.close()

#comando a usar para decifrar o texto encriptado pela ferramenta no repositorio https://github.com/jforissier/aesgcm é
# ./aesgcm dec -key key.txt -iv iv.txt -in encrypted_aesgcm.txt -tag tag.txt -out decrypted_aesgcm.txt

#Aes gcm (Galois Counter Mode) baseia-se no aes Counter Mode com a adição de um parametro de autenticação que torna a encriptação
# e decriptação em etapas autenticadas. A chave de aes gcm é gerada a partir do nonce e da palavra chave escolhida pelo
# utilizador. No caso do aes ctr a chave era generada de forma aleatória.