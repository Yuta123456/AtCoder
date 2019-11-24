h, w = map(int, input().split())
if h % 3 == 0 or w % 3 == 0:
    print(0)
    exit()
else:
    middle = w // 2
    ans = 10 ** 10
    for i in range(1,h):
        area = [i * w, (h - i) * middle, (h - i) * (w - middle)]
        ans = min(ans, max(area) - min(area))
print(ans)