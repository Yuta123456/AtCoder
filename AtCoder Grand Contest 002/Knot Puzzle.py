from collections import deque
n, l = map(int, input().split())
a = list(map(int, input().split()))
que = deque(a)
n -= 1
left_count = 1
right_count = n
ans = []
sum_length = sum(a)
while sum_length >= l and n > 0:
    left = que.popleft()
    right = que.pop()
    if left < right:
        que.append(right)
        sum_length -= left
        ans.append(left_count)
        left_count += 1
    else:
        que.appendleft(left)
        sum_length -= right
        ans.append(right_count)
        right_count -= 1
    n -= 1
if n == 0:
    print("Possible")
    for i in range(len(ans)):
        print(ans[i])
else:
    print("Impossible")