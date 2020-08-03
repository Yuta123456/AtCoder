from collections import Counter
n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
q = int(input())
data = []
ans = sum(a)
for i in range(q):
    b, c = map(int, input().split())
    ans += count[b] * (c - b)
    if b in count : 
        count[c] += count[b]
        count[b] = 0
    print(ans)
