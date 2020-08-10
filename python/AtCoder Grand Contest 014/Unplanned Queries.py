n, m = map(int, input().split())
count = [0 for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    count[a] += 1
    count[b] += 1
for i in range(n+1):
    if count[i] % 2 != 0:
        print("NO")
        exit()
print("YES")
