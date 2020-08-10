import sys
input = sys.stdin.readline
n,k = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0
for i in range(n-k+1):
    flag = 1
    for j in range(i+1,i+k):
        if a[j] <= a[j-1]:
            flag = 0
            break
    if flag:
        ans += 1
print(ans)