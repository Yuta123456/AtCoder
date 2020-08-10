from collections import Counter
n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
for i in range(1,n+1):
    print(count[i])