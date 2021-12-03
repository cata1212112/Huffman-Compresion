from huff import Huffman_Tree
import sys

head = open("header.bin", "rb")
compressed = sys.argv[1]
output = sys.argv[2]

cati = head.read(4)
cati = int.from_bytes(cati, 'little')

first = head.read(1)
second = head.read(4)

freq = {}
invers = {}

sum = 0
while first:
    freq[first] = int.from_bytes(second, 'little')
    sum += freq[first]

    first = head.read(1)
    second = head.read(4)

head.close()

huff = Huffman_Tree(freq, sum)
coduri = huff.get_coduri()

for x in coduri:
    invers[x[1]] = x[0]

comprimat = open(compressed, "rb")
out = open(output, "wb")

str = ""

vec = [0b10000000, 0b01000000, 0b00100000, 0b00010000, 0b00001000, 0b00000100, 0b00000010, 0b00000001]

cnt = 0
byte = comprimat.read(1)
while byte:
    dap = int.from_bytes(byte, 'little')
    for x in vec:
        acm = (dap & x)
        if acm != 0:
            str += "1"
        else:
            str += "0"
        cnt += 1
        if cnt > cati:
            break
        if str in invers:
            out.write(invers[str])
            str = ""
    if cnt > cati:
        break
    byte = comprimat.read(1)

comprimat.close()
out.close()