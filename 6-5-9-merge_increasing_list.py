import math
import random

class Node:
    def __init__(self):
        self.key = None
        self.next = None
    def __lt__(self,other):
        if self.key < other.key:
            return True
        return False

class MinHeap:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def parent(self, i):
        return math.floor((i-1)/2)

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def min_heapify(self, i):
        while True:
            l = self.left(i)
            r = self.right(i)

            if l<len(self.heap) and self.heap[l]<self.heap[i]:
                smallest = l
            else:
                smallest = i
            if r<len(self.heap) and self.heap[r]<self.heap[smallest]:
                smallest = r

            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def build_min_heap(self):
        self.heap_size = len(self.heap)
        for i in range(math.floor(len(self.heap)/2)-1, -1, -1):
            self.min_heapify(i)
    
    def heap_delete_min(self):
        self.heap[0] = self.heap[-1]
        del(self.heap[-1])
        self.heap_size -= 1
        self.min_heapify(0)

    def heap_minimum(self):
        return self.heap[0]

    def heap_min_next(self):
        if self.heap[0].next != None:
            self.heap[0] = self.heap[0].next
            self.min_heapify(0)
        else:
            self.heap_delete_min()

result = []
all_list = []

for i in range(0,10):
    L = random.sample(range(0,100), 10)
    L = sorted(L)
    print(L)
    head = Node()
    for j in range(len(L)-1,-1,-1):
        node = Node()
        node.key = L[j]
        node.next = head.next
        head.next = node
    all_list.append(head)

min_heap = MinHeap()
for i in range(0,len(all_list)):
    min_heap.heap.append(all_list[i].next)
min_heap.build_min_heap()
while(min_heap.heap_size>0):
    smallest = min_heap.heap_minimum()
    result.append(smallest.key)
    min_heap.heap_min_next()

print(result)
