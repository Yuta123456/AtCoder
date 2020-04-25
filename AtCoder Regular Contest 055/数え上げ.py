n = int(input())
ans = "7"
for i in range(n-1):
    ans = "0" + ans
ans = "1" + ans
print(ans)