t = int(input())

mod = 10**9 + 7
for _ in range(t):
    n, a, b = map(int, input().split())
    red = (n + 1 - a)**2
    blue = (n + 1 - b) ** 2
    ans = red * blue
    if a > b:
        a,b = b, a
    # 大部分
    over = (n - 2*a - b + 1) * (n - 2*a - b + 1)
    if over < 0: 
        over = 0
    tmp = (a + 1) * (b + 1) * over
    
    