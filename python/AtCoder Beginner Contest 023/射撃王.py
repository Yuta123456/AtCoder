n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
def binary_search(left, right):
    if right - left <= 1:
        return right
    middle = (right + left)//2
    if is_can(middle):
        return binary_search(left,middle)
    else:
        return binary_search(middle,right)
def is_can(limit):
    data.sort(key=lambda x: (limit - x[0] + x[1]) / x[1])
    for i in range(n):
        if data[i][0] + data[i][1] * i > limit:
            return False
    return True
print(binary_search(0,10**15))