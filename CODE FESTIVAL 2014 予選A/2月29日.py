a,b = map(int, input().split())
all_4 = 0
all_100 = 0
all_400 = 0
if a % 4 == 0:
    all_4 += 1

if a % 100 == 0:
    all_100 += 1
if a % 400 == 0:
    all_400 += 1
all_4 += (b // 4) - (a // 4)
all_100 += (b // 100) - (a // 100)
all_400 += (b // 400) - (a // 400)

print(all_4 - all_100 + all_400)