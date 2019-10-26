import random

max_integer = int(input('integer scope:0-? ')) + 1
length = int(input('how many integers? '))
A = []
if length <= max_integer + 1:
    A = random.sample(range(0, max_integer), length)
else:
    for i in range(0,length):
        A.append(random.randrange(0, max_integer))

def partition(A,p,r):
    k = random.randint(p,r)
    A[k],A[r]=A[r],A[k]

    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quick_sort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)

def partition2(A,p,r):
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        j -= 1
        while A[j]>x:
            j -= 1
        i += 1
        while A[i]<x:
            i += 1
        if i<j:
            A[i],A[j] = A[j],A[i]
        else:
            return j

def quick_sort2(A,p,r):
    if p<r:
        q = partition2(A,p,r)
        quick_sort2(A,p,q)
        quick_sort2(A,q+1,r)

def partition3(A,p,r):
    x = A[r]
    A[p],A[r]=A[r],A[p]
    i = p-1
    k = p
    for j in range(p+1,r+1):
        if A[j] < x:
            i += 1
            A[i],A[j]=A[j],A[i]
            k += 1
            A[k],A[j]=A[j],A[k]
        elif A[j]==x:
            k += 1
            A[k],A[j]=A[j],A[k]
    return i+1,k

def quick_sort3(A,p,r):
    if p<r:
        q,t = partition3(A,p,r)
        quick_sort3(A,p,q-1)
        quick_sort3(A,t+1,r)

def partition4(A,p,r):
    x = A[p]
    i = p
    j = r
    while(i<j):
        while(i<j and A[j]>=x):
            j-=1
        A[i]=A[j]
        while(i<j and A[i]<=x):
            i+=1
        A[j]=A[i]
    A[i]=x
    return i

def quick_sort4(A,p,r):
    if p<r:
        q = partition4(A,p,r)
        quick_sort4(A,p,q-1)
        quick_sort4(A,q+1,r)

def quick_sort_tail_recursive(A, p, r):
    while p<r:
        q = partition(A, p, r)
        quick_sort_tail_recursive(A, p, q-1)
        p = q+1

print('before sort:')
print(A)
quick_sort4(A,0,len(A)-1)
print('after sort:')
print(A)
