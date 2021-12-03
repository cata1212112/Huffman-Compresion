from queue import PriorityQueue
import math
import sys

class Huffman_Node:
    def __init__(self, prob, caracter):
        self.left = None
        self.right = None
        self.caracter = caracter
        self.prob = prob

    def __lt__(self, other):
        return self.prob < other.prob

class Huffman_Tree:
    def __init__(self, freq, sum):
        self.freq = freq
        self.sum = sum

    def Build(self):
        q = PriorityQueue()
        for x in self.freq:
            q.put(Huffman_Node(self.freq[x]/self.sum, x))

        while q.qsize() > 1:
            a = q.get()
            b = q.get()

            c = Huffman_Node(a.prob + b.prob, a.caracter + b.caracter)

            c.left = a
            c.right = b
            q.put(c)
        return q.get()

    def DFS(self, nod, cod, coduri):
        if nod.left == None and nod.right == None:
            coduri.append((nod.caracter, cod))
        else:
            if nod.left != None:
                self.DFS(nod.left, cod + "1", coduri)

            if nod.right != None:
                self.DFS(nod.right, cod + "0", coduri)

    def get_coduri(self,):
        coduri = []
        radacina = self.Build()
        self.DFS(radacina, "", coduri)
        return coduri