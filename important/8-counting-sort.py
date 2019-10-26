import random

max_integer = int(input('integer scope:0-? ')) + 1
length = int(input('how many integers? '))
A = []
if length <= max_integer + 1:
    A = random.sample(range(0, max_integer), length)
else:
    for i in range(0,length):
        A.append(random.randrange(0, max_integer))

def counting_sort(A,B,k):
    C = [0]*(k+1)
    for j in range(0,len(A)):
        C[A[j]]+=1
    for i in range(1,len(C)):
        C[i]+=C[i-1]
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1]=A[j]
        C[A[j]]-=1

B = [0]*len(A)
print('before sorting:')
print(A)
counting_sort(A,B,max_integer-1)
print(B)
