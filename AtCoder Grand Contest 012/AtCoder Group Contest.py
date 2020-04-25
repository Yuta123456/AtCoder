n = int(input())
a = list(map(int, input().split()))
a.sort()
print(sum([a[i] for i in range(n,3*n,2)]))