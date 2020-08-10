x = int(input())
ans = x // 500
x -= ans * 500
ans *= 1000
ans += (x // 5) * 5
print(ans)