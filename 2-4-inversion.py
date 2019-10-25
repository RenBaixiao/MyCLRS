import random

max_integer = int(input('integer scope: 0-? ')) + 1
length = int(input('how many integers? '))
A = []
if length <= max_integer + 1:
    A = random.sample(range(0, max_integer), length)
else:
    print('length must be less than max_integer')
    sys.exit(0)
print(A)

def merge_inversions(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]

    i=0
    j=0
    k=p
    inversions = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inversions += len(L) - i
        k += 1

    if j == len(R):
        A[k:r+1] = L[i:]
    
    return inversions

def count_inversions(A, p, r):
    inversions= 0
    if p < r:
        q = (p+r) // 2
        inversions += count_inversions(A, p, q)
        inversions += count_inversions(A, q+1, r)
        inversions += merge_inversions(A, p, q, r)
    return inversions

inversions = count_inversions(A, 0, len(A)-1)
print('inversion_count: ' + str(inversions))
