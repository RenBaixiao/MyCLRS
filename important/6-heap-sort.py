import math
import random

max_integer = int(input('integer scope:0-?')) + 1
length = int(input('how many integers? '))
A = []
if length <= max_integer + 1:
    A = random.sample(range(0, max_integer), length)
else:
    for i in range(0,length):
        A.append(random.randrange(0, max_integer))

def parent(i):
    return math.floor((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def min_heapify(A,i,heap_size):
    l = left(i)
    r = right(i)

    if l<heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r<heap_size and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[i],A[smallest] = A[smallest],A[i]
        min_heapify(A,smallest,heap_size)

def max_heapify_iteration(A,i,heap_size):
    while True:
        l = left(i)
        r = right(i)

        if l<heap_size and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r<heap_size and A[r] > A[largest]:
            largest = r

        if largest != i:
            A[i],A[largest] = A[largest],A[i]
            i = largest
        else:
            break

def build_max_heap(A):
    for i in range(math.floor(len(A)/2)-1,-1,-1):
        max_heapify_iteration(A,i,len(A))

def heap_sort(A):
    build_max_heap(A)
    heap_size = len(A)
    for i in range(len(A)-1,0,-1):
        A[0],A[i] = A[i],A[0]
        heap_size -= 1
        max_heapify_iteration(A,0,heap_size)

print('before sorting:')
print(A)
heap_sort(A)
print('after sorting:')
print(A)
