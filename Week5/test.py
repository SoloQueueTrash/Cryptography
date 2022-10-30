# Exercicio 1
from binascii import unhexlify, hexlify
from data import *
import numpy as np

def xor_op(packet1, packet2):
    return bytes([a ^ b for a, b in zip(packet1, packet2)])

xor_packets = []
counter = 0
result = []

for i in range(0, len(packets)):
    for j in range(i + 1, len(packets)):
        xor_packets = list(xor_op(unhexlify(packets[i]), unhexlify(packets[j])))

        for k in range(0, len(xor_packets)):
            if(xor_packets[k] < 128): 
                counter += 1

        if(counter == len(xor_packets)):
            result.append(i)
            result.append(j)
            #print("[", i, ", ", j, "]")

        counter = 0

#print(result)
print(np.unique(result))