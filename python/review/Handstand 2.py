n = int(input())
memo = dict()
for i in range(1,n+1):
    string_i = str(i)
    com = (string_i[0], string_i[-1])
    if com in memo:
        memo[com] += 1
    else:
        memo[com] = 1
ans = 0
for i in range(1,n+1):
    string_i = str(i)
    com = (string_i[-1], string_i[0])
    if com in memo:
        ans += memo[com]
print(ans)