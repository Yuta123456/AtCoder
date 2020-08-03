from bisect import bisect_right
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
#小さい値からk個目の値を出力
def binary_search(left, right):
    if right - left <= 1:
        return right
    middle = (right + left) // 2
    if not is_can(middle):
        return binary_search(middle, right)
    else:
        return binary_search(left, middle)
def is_can(target):
    count = 0
    for i in range(n):
        num = target // a[i]
        index = bisect_right(b, num)
        count += index
    if count >= k:
        return True
    else:
        return False
print(binary_search(0, 10**19))
