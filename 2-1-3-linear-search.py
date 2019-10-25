import random

max_integer = int(input('integer scope: 0-? ')) + 1
length = int(input('how many integers? '))
A = []
if length <= max_integer + 1:
    A = random.sample(range(0, max_integer), length)
else:
    for i in range(0, length):
        A.append(random.randrange(0, max_integer))
print(A)

def linear_search(A, key):
    for i in range(0, len(A)):
        if A[i]==key:
            return i
    return 'NIL'

key = int(input('integer to search: '))
index = linear_search(A, key)
print(index)
