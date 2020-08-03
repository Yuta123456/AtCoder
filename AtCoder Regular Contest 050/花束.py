r, b = map(int, input().split())
x, y = map(int, input().split())
ans = max(min(r, b//y), min(b, r//x))
k = (b - y*r)//(1 - x*y)
for i in range(k-2,k+3):
    use_r = r - i * x
    use_b = b - i
    l = min(use_r, use_b//y)
    if i * x + l <= r and l*y + i <= b and i >= 0 and l >= 0:
        ans = max(ans, l + i)
print(ans)