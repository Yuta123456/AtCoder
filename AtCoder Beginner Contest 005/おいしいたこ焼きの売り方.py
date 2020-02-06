import bisect
t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
pre = -1
for i in range(m):
    k = B[i]
    flag = True
    for j in range(len(A)):
        if k - t <= A[j] <= k:
            del A[j]
            flag = False
            break
    if flag:
        print("no")
        exit()
print("yes")
        
