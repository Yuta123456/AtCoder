h = int(input())

ans = 0
count = 0
while h > 0:
    ans += (2 ** count)
    count += 1
    h = h//2
print(ans)