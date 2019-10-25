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

def merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))

    i = 0
    j = 0
    k = p

    while k <= r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def find_two_value_sum(A, x):
    low = 0
    high = len(A) - 1
    while low < high:
        sum_value = A[low] + A[high]
        if sum_value == x:
            return A[low], A[high]
        elif sum_value > x:
            high -= 1
        else:
            low += 1
    return None, None

x = int(input('the sum value x: '))
merge_sort(A, 0, len(A)-1)
num1, num2 = find_two_value_sum(A, x)
if num1 == None:
    print('not exist')
else:
    print(str(num1) + ' + ' + str(num2) + ' = ' + str(x))
