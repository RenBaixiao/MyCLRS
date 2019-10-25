import random

max_integer = int(input('integer scope:0-? ')) + 1
length = int(input('how many integers? '))

A = []
if length <= max_integer + 1:
    A = random.sample(range(0, max_integer), length)
else:
    for i in range(0, length):
        A.append(random.randrange(0, max_integer))

print('before sorting:')
print(A)

def selection_sort(A):
    for j in range(0,len(A)-1):
        smallest = j
        for i in range(j+1,len(A)):
            if A[i] < A[smallest]:
                smallest = i
        A[j],A[smallest] = A[smallest],A[j]

selection_sort(A)
print('after sorting:')
print(A)
