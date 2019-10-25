import math

def heap_minimum(A):
    return A[0]

def parent(i):
    return math.floor((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def min_heapify(A,i):
    while True:
        l = left(i)
        r = right(i)

        if l<len(A) and A[l]<A[i]:
            smallest = l
        else:
            smallest = i
        if r<len(A) and A[r]<A[smallest]:
            smallest = r

        if smallest != i:
            A[i],A[smallest] = A[smallest],A[i]
            i = smallest
        else:
            break

def heap_extract_min(A):
    if len(A) < 1:
        print('heap underflow')
        return

    minimum = A[0]
    A[0] = A[-1]
    del(A[-1])
    min_heapify(A,0)
    return minimum

def heap_decrease_key(A,i,key):
    if key > A[i]:
       print('new key is larger than current key') 
    A[i] = key
    while i>0 and A[parent(i)]>A[i]:
        A[i],A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

def heap_decrease_key_2(A,i,key):
    if key > A[i]:
        print('new key is larger than current key')
    while i>0 and A[parent(i)]>key:
        A[i] = A[parent(i)]
        i = parent(i)
    A[i] = key

def min_heap_insert(A,key):
    A.append(float('INF'))
    heap_decrease_key(A,len(A)-1,key)

def min_heap_delete(A,i):
    temp = A[i]
    heap_decrease_key_2(A,i,float('-inf'))
    A[0] = A[-1]
    del(A[-1])
    min_heapify(A,0)
    return temp
