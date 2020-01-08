import copy
import math
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort()
A.reverse()
maxX = max(F) * max(A)
def is_able(low, up):
    target = (low + up) // 2
    if low == up - 1:
        return up
    if check(target):
        return is_able(low, target)
    else:
        return is_able(target, up)
def check(time):
    #time が可能かどうか
    practice = copy.deepcopy(k)
    for i in range(n):
        if A[i] * F[i] > time:
            practice -= A[i] - math.floor(time / F[i]) 
            if practice < 0:
                return False
    return True
print(is_able(-1, maxX))