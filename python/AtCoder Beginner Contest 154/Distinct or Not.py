n = int(input())
a = list(map(int, input().split()))
k = set(a)
if len(k) == len(a):
    print("YES")
else:
    print("NO")