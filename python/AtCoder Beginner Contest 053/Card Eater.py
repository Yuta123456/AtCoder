n = int(input())
a = list(map(int, input().split()))
m = len(set(a))
if n % 2 == m % 2:
    print(m)
else:
    print(m - 1)