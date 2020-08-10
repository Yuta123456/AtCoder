n,m,v,p = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
def binary_search(left, right):
    if right - left <= 1:
        return left
    middle = (left + right) // 2
    if check(middle):
        return binary_search(middle, right)
    else:
        return binary_search(left, middle)

def check(target):
    used_vote = (p + n - target - 1) * m
    sum_vote = 0
    for i in range(target-1, p-2, -1):
        if a[target] + m < a[i]:
            return False
        sum_vote += (a[target] + m) - a[i]
    if sum_vote >= (m * v - used_vote): 
        return True
    else:
        return False
print(binary_search(0,n) + 1)