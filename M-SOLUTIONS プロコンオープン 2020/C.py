from collections import deque
n , k = map(int, input().split())
a = list(map(int, input().split()))
que = deque()
for i in range(k):
    que.append(a[i])
for i in range(k, n):
    if a[i] > que.popleft():
        print("Yes")
    else:
        print("No")
    que.append(a[i])