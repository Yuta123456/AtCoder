x, n = map(int, input().split())
a = set(list(map(int, input().split())))
ans_d = 10000
ans = -1
for i in range(-100,1000):
    if abs(x - i) < ans_d and i not in a:
        ans = i
        ans_d = abs(x - i)
print(ans)
