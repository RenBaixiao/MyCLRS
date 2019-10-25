import random

max_integer = int(input('integer scope -x ~ x, input x: ')) + 1
length = int(input('how many integers? '))
A = []
if length <= max_integer + 1:
    A =  random.sample(range(-max_integer+1, max_integer), length)
else:
    for i in range(0, length):
        A.append(random.randrange(-max_integer+1, max_integer))
print(A)

def find_maximum_subarray(A):
    max_sum = float('-inf')
    temp_sum = float('-inf')
    for i in range(0, len(A)):
        current_high = i
        if temp_sum > 0:
            temp_sum += A[i]
        else:
            current_low = i
            temp_sum = A[i]

        if temp_sum > max_sum:
            max_sum = temp_sum
            low = current_low
            high = current_high

    return low, high, max_sum

low, high, max_sum = find_maximum_subarray(A)
print(low, high, max_sum)
