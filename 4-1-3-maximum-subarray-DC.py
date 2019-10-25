import random

max_integer = int(input('integer scope -x ~ x, input x: ')) + 1
length = int(input('how many integers? '))
A = []
if length <= max_integer + 1:
    A = random.sample(range(-max_integer+1, max_integer), length)
else:
    for i in range(0, length):
        A.append(random.randrange(-max_integer-1, max_integer))
print(A)

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    temp_sum = 0
    
    for i in range(mid, low-1, -1):
        temp_sum += A[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = i

    right_sum = float('-inf')
    temp_sum = 0

    for j in range(mid+1, high+1):
        temp_sum += A[j]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right = j

    return max_left, max_right, left_sum + right_sum

def find_maximum_subarray(A, low, high):
    if low < high:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        if left_sum > right_sum and left_sum > cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum
    else:
        return low, high, A[low]

low, high, max_sum = find_maximum_subarray(A, 0, len(A)-1)
print(low, high, max_sum)
