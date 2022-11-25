import sys
import numpy as np
from sage.all import *

def rsa_decrypt(c, e, phi, n):
    xgcd1 = xgcd(e, phi)
    d = xgcd1[1]
    
    if(xgcd1[1] < 0): 
        d = phi + xgcd1[1]

    return (c ** d) % n

def phi(p, q):
    return (p - 1) * (q - 1)

ciphertext = 20
e = 13
n = 77
ph = phi(11, 7) #fatorizar n: 77 = {7, 11}

message = rsa_decrypt(ciphertext, e, ph, n)
print(message)

