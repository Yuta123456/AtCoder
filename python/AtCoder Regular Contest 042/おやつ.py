n, p = map(int, input().split())
snack = []
for i in range(n):
    snack.append(list(map(int, input().split())))
#はみ出す値段の探索
ans = 0
for i in range(101):
    sum_value = 0
    for j in range(n):
        if snack[j][0] >= i:
            sum_value += snack[j][1]
    ans = max(ans, sum_value)
print(ans)
