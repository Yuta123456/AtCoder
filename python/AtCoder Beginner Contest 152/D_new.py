n = int(input())
memo = [[0 for i in range(10)] for j in range(10)]
for i in range(1,n+1):
    i_first = int(str(i)[0])
    i_last = int(str(i)[-1])
    memo[i_first][i_last] += 1
ans = 0
for i in range(1,n+1):
    i_first = int(str(i)[0])
    i_last = int(str(i)[-1])
    ans += memo[i_last][i_first]
print(ans)