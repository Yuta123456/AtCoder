import copy
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort()
A.reverse()
maxX = max(F) * max(A)
print(A)
print(F)
x = [-1 for i in range(maxX + 1)]
def is_able(low, up):
    target = (low + up) // 2
    print("{} {}".format(low, up))

    if x[target] == 1 and x[target + 1] == 0:
        return target
    if check(target):
        x[target] = 1
        return is_able(low, target)
    else:
        x[target] = 0
        return is_able(target, up)
def check(time):
    #time が可能かどうか
    practice = copy.deepcopy(k)
    for i in range(n):
        if A[i] * F[i] > time:
            practice -= A[i]  + 1 - ( time / F[i] ) 
            if practice < 0:
                return False
    return True
x[0] = int(check(0))
x[maxX] = int(check(maxX))
#print(is_able(0, maxX))