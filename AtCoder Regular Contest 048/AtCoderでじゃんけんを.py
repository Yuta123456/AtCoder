import bisect
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())) + [i])
data.sort(reverse=True)
#sort, 二分探索、累積和でツモ
ans = []
print(data)
#for i in range(n):
