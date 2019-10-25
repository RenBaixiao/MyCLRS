import random

max_integer = int(input('integer scope -x ~ x, input x: ')) + 1
length = int(input('how many integers? '))
A = []
if length <= max_integer + 1:
    A = random.sample(range(-max_integer+1, max_integer), length)
else:
    for i in range(0, length):
        A.append(random.randrange(-max_integer+1, max_integer))
print(A)

def find_maximum_subarray(A):
    max_sum = float('-inf')
    for i in range(0, len(A)):
        temp_sum = 0
        for j in range(i, len(A)):
            temp_sum += A[j]
            if temp_sum > max_sum:
                low = i
                high = j
                max_sum = temp_sum
    return low, high, max_sum

low, high, max_sum = find_maximum_subarray(A)
print(low, high, max_sum)
