from collections import deque
n, k = map(int, input().split())
a = list(map(int, input().split()))
#kを法とする配列を作る
a = [(i - 1) for i in a]
acc_a = [0 for i in range(n+1)]
acc_a[0] = 0
acc_a[1] = a[0] % k
#kを法とする累積和
for i in range(2,len(a) + 1):
    acc_a[i] = (a[i - 1] + acc_a[i-1]) % k
ans = 0
count = {}
q = deque()
for i in acc_a:
    if i not in count:
        count[i] = 0
    ans += count[i]
    count[i] += 1
    q.append(i)
    if len(q) == k:
        count[q.popleft()] -= 1
print(ans)