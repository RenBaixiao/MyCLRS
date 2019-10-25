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

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

insertion_sort(A)
print('after sorting:')
print(A)
