from queue import PriorityQueue
import math
import sys
from huff import Huffman_Tree

inp = sys.argv[1]
out = sys.argv[2]

input = open(inp, "rb")

biti_initiali = 0

freq = {}
sum = 0
bytes = 0
byte = input.read(1)

while byte:
    bytes += 1
    sum += 1
    if byte not in freq:
        freq[byte] = 1
    else:
        freq[byte] += 1
    byte = input.read(1)

huff = Huffman_Tree(freq, sum)
coduri = huff.get_coduri()

map = {}
biti = 0
final = 0

out = open(out, "wb")

input = open(inp, "rb")
compresie = ""
byte = input.read(1)

for x in coduri:
    map[str(x[0])] = x[1]

while byte:
    compresie += map[str(byte)]
    byte = input.read(1)

head = open("header.bin", "wb")
biti_initiali = len(compresie)
head.write(biti_initiali.to_bytes(4, byteorder='little'))

for x in freq:
    head.write(x)
    head.write(freq[x].to_bytes(4,byteorder='little'))

for i in range((8 - len(compresie)%8)%8):
    compresie += "0"

def to_char(byte):
    i = 7
    putere = 1
    rez = 0
    while i >= 0:
        if byte[i] == '1':
            rez += putere
        putere *= 2
        i -= 1
    return rez

rez = bytearray()
for i in range(0, len(compresie) - 7, 8):
    rez.append(to_char(compresie[i:i+8]))

out.write(rez)
out.close()
head.close()