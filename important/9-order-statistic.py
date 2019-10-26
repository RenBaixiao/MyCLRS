import random

max_integer = int(input('integer scope: 0-? ')) + 1
length = int(input('how many integers? '))
A = []
if length <= max_integer + 1:
    A = random.sample(range(0, max_integer), length)
else:
    for i in range(0,length):
        A.append(random.randrange(0, max_integer))

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def select(A, p, r, i):
    if p==r:
        return A[p]
    q = partition(A, p, r)
    k = q-p+1
    if i==k:
        return A[q]
    elif i<k:
        return select(A, p, q-1, i)
    else:
        return select(A, q+1, r, i-k)

def select_loop(A, p, r, i):
    while p<r:
        q = partition(A, p, r)
        k = q-p+1
        if i==k:
            return A[q]
        elif i<k:
            r = q-1
        else:
            p = q+1
            i -= k
    return A[p]

order = int(input('which order_statistic to find? 1-' + str(length) +': '))
print('before select:')
print(A)
statistic = select_loop(A,0,len(A)-1,order)
print(str(order)+'th statistic:')
print(statistic)
