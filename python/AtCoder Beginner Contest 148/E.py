n = int(input())
if n % 2 == 1:
    print(0)
    exit()
else:
    ans = 0
    keta = 1
    while n >= (5**keta):
        ans += (n // (5**keta))//2
        keta += 1
    keta = 1
print(ans)
