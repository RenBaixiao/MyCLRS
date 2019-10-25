import random

max_integer = int(input('integer scope: 0-? ')) + 1
length = int(input('how many integers? '))
A = []
if length <= max_integer + 1:
    A = random.sample(range(0, max_integer), length)
else:
    for i in range(0, max_integer):
        A.append(random.randrange(0, max_integer))
print('before sorting')
print(A)

def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]

bubble_sort(A)
print('after sorting')
print(A)
