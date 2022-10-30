import hmac
import hashlib
from binascii import hexlify 
from os import urandom

key = urandom(16)
file = open("plaintext.txt", "rb")
message = file.read()

dig = hmac.new(key, msg=bytes(message), digestmod=hashlib.sha256).hexdigest()

output = open("decrypt_sha2.txt", "w")
print(dig)
output.write(dig)

key_file = open("key_sha2.txt", "wb")
key_file.write(hexlify(key))

file.close()
output.close()
key_file.close()