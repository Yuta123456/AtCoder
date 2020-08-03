from bisect import bisect_left
n, l = map(int, input().split())
dp = [10**13 for i in range(l+1)]
dp[0] = 0
x = list(map(int, input().split())) + [10**6 for i in range(5)]
t = list(map(int, input().split()))
for i in range(l):
    near_hardle_index = bisect_left(x, i+1)
    #普通に走っていく
    #行った先にハードルがあった場合は乗り越えるしかない
    if x[near_hardle_index] == i+1:
        dp[i+1] = min(dp[i+1], dp[i] + t[0] + t[2])
    else:
        dp[i+1] = min(dp[i+1], dp[i] + t[0])
    
    #行動2をする
    #行った先にハードルがあった場合は乗り越えるしかない
    if i + 2 > l:
        dp[l] = min(dp[l], dp[i] + (t[0]//2) + (t[1]//2))
    else:
        if x[near_hardle_index] == i+2 or x[near_hardle_index + 1] == i+2:
            dp[i+2] = min(dp[i+2], dp[i] + t[0] + t[2] + t[1])
        else:
            dp[i+2] = min(dp[i+2], dp[i] + t[0] + t[1])
    #行動3をする
    #行った先にハードルがあった場合は乗り越えるしかない
    if i + 4 > l:
        dp[l] = min(dp[l], dp[i] + (t[0] // 2) + t[1] * (l - i - 0.5))
    else:
        flag = False
        for tmp in range(near_hardle_index, near_hardle_index+4):
            if x[tmp] == i + 4:
                flag = True
        if flag:
            dp[i+4] = min(dp[i+4], dp[i] + t[0] + t[2] + t[1] * 3)
        else:
            dp[i+4] = min(dp[i+4], dp[i] + t[0] + t[1] * 3)

print(int(dp[l]))
    