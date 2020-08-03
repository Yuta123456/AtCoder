from bisect import bisect_left
n = int(input())
c = []
for i in range(n):
    c.append(int(input()))
lis = [10**9 for i in range(n+1)]
lis[1] = c[0]
lis[0] = -10**9
for i in c:
    index = bisect_left(lis, i)
    lis[index] = i
print(n - lis.index(max([i for i in lis if i != 10**9])))
