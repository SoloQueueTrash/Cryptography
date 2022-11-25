import sys
import numpy as np
from sage.all import *

def rsa_key(e, phi):
    return xgcd(e, phi)[1]

def phi(p, q):
    return (p - 1) * (q - 1)

ciphertext = 20
e = 65
n = 2881
ph = phi(43, 67) #fatorizar n: 2881 = {43, 67}

key = rsa_key(e, ph)
print(key)

