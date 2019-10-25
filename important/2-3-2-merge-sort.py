import random

max_integer = int(input('integer scope:0-? ')) + 1
length = int(input('how many integers? '))
A = []
if length <= max_integer + 1:
    A = random.sample(range(0, max_integer), length)
else:
    for i in range(0,length):
        A.append(random.randrange(0, max_integer))

def merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    
    i = 0
    j = 0
    k = p

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    if j == len(R):
        A[k:r+1] = L[i:]

def merge_sort(A, p, r):
    if p<r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

print('before sorting:')
print(A)

merge_sort(A, 0, len(A)-1)

print('after sorting:')
print(A)
