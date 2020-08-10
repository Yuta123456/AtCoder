n, k = map(int, input().split())
r,s,p = map(int, input().split())
t = input()
ans = 0
get_point = {}
get_point["r"] = p
get_point["s"] = r
get_point["p"] = s
string = [[] for i in range(k)]
for i in range(n):
    string[i%k].append(t[i])
for i in range(len(string)):
    dp = [[0 for q in range(3)] for z in range(len(string[i]))]
    if string[i][0] == "r":
        dp[0][2] = get_point[string[i][0]]
    elif string[i][0] == "s":
        dp[0][0] = get_point[string[i][0]]
    else:
        dp[0][1] = get_point[string[i][0]]
    for j in range(1,len(string[i])):
        if string[i][j] == "r":
            dp[j][0] = max(dp[j-1][1], dp[j-1][2])
            dp[j][1] = max(dp[j-1][0], dp[j-1][2]) 
            dp[j][2] = max(dp[j-1][0], dp[j-1][1]) + get_point[string[i][j]]
        elif string[i][j] == "s":
            dp[j][0] = max(dp[j-1][1], dp[j-1][2]) + get_point[string[i][j]]
            dp[j][1] = max(dp[j-1][0], dp[j-1][2]) 
            dp[j][2] = max(dp[j-1][0], dp[j-1][1]) 
        else:
            dp[j][0] = max(dp[j-1][1], dp[j-1][2])
            dp[j][1] = max(dp[j-1][0], dp[j-1][2]) + get_point[string[i][j]]
            dp[j][2] = max(dp[j-1][0], dp[j-1][1])
    ans += max(dp[-1])
print(ans)
        

        




