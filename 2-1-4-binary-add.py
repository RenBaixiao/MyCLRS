import random

n = int(input('how many digits? '))

A = []
B = []

for i in range(0,n):
    digit = random.randint(0,1)
    A.append(digit)
    digit = random.randint(0,1)
    B.append(digit)

print(A)
print(B)

add = 0
C = [0]*(n+1)

for i in range(n-1,-1,-1):
    digit_sum = A[i] + B[i] + add
    add = digit_sum // 2
    C[i+1] = digit_sum % 2

C[0]=add

print(C)
