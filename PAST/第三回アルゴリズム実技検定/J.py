from bisect import bisect_right
n,m = map(int, input().split())
#出来る配列は単調減少
sushi = list(map(int, input().split()))
array = [10**10 for i in range(n+1)]
for i in range(m):
    index = bisect_right(array, -sushi[i])
    if index == n:
        print(-1)
    else:
        print(index+1)
        array[index] = -sushi[i]
