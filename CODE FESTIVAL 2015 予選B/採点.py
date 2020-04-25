from collections import Counter
n,m = map(int, input().split())
a = list(map(int, input().split()))
count = Counter(a)
max_count = max([(count[i], i) for i in count.keys()], key=lambda x: x[0])
if max_count[0] > n / 2:
    print(max_count[1])
else:
    print("?")