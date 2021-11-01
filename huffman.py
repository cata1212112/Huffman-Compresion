from queue import PriorityQueue
import math

inp = "text"
out = "data"

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

class Huffman:
    def __init__(self, prob, caracter):
        self.left = None
        self.right = None
        self.caracter = caracter
        self.prob = prob

    def __lt__(self, other):
        return  self.prob < other.prob

def Build():
    q = PriorityQueue()
    for x in freq:
        q.put(Huffman(freq[x]/sum, str(x)))

    while q.qsize() > 1:
        a = q.get()
        b = q.get()

        c = Huffman(a.prob + b.prob, a.caracter + b.caracter)

        c.left = a
        c.right = b
        q.put(c)
    return q.get()

coduri = []
def DFS(nod, cod):
    if nod.left == None and nod.right == None:
        coduri.append((nod.caracter, cod))
    else:
        if nod.left != None:
            DFS(nod.left, cod + "1")

        if nod.right != None:
            DFS(nod.right, cod + "0")


radacina = Build()
DFS(radacina, "")

map = {}
biti = 0
final = 0


out = open(out, "wb")

input = open(inp, "rb")
compresie = ""
byte = input.read(1)

for x in coduri:
    map[str(x[0])] = x[1]
    print(x)

while byte:
    compresie += map[str(byte)]
    byte = input.read(1)

for i in range((8 - len(compresie)%8)%8):
    compresie += "0"

entropie_shanon = 0
for y in freq:
    entropie_shanon += freq[y]/sum * math.log2(sum/freq[y])

print(f"Entropia Shanon este {entropie_shanon}")

entropie_huffman = 0
for y in freq:
    biti += freq[y] * len(map[str(y)])
    entropie_huffman += freq[y]/sum * len(map[str(y)])

print(f"Entropia codului Huffman este {entropie_huffman}")
print(f"Numarul initial de biti este {bytes*8}")
print(f"Numarul final de biti este {biti}")

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
