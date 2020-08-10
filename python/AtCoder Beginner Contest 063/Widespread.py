import math
n, a, b = map(int, input().split())
h = []
spread = b
attack = a - b
count = 0
for i in range(n):
    h.append(int(input()))
h.sort()
h.reverse()
def binary_search(left, right):
    if right - left <= 1:
        return right
    middle = (right + left)//2
    count = 0
    for i in range(n):
        if h[i] - (middle * spread) <= 0:
            break
        else:
            count += math.ceil((h[i] - (middle * spread)) / attack)
    if count > middle:
        return binary_search(middle, right)
    elif count < middle:
        return binary_search(left, middle)
    else:
        return middle
print(binary_search(0,10**10))

