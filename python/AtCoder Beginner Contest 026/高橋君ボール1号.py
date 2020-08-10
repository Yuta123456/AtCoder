import math
a,b,c = map(int, input().split())
def binary_search(left, right):
    middle = (left + right) / 2
    if abs(100 - (a * middle + b * math.sin(c * middle * math.pi))) > 10**(-7):
        if 100 - (a * middle + b * math.sin(c * middle * math.pi)) < 0:
            return binary_search(left, middle)
        else:
            return binary_search(middle, right)
    else:
        return middle
print(binary_search(0,10**18))