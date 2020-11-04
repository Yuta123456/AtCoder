n = int(input()) + 1
d = [0] + list(map(int, input().split()))
ans = 0
def dfs(time_set,index):
    # print("{} {}".format(time_set, index))
    if len(time_set) >= n:
        time_list = list(time_set)
        time_list.sort()
        cand = min(time_list[-1] - time_list[0], 24 + time_list[0] - time_list[-1])
        global ans
        for i in range(1,n):
            cand = min(cand, time_list[i] - time_list[i-1])
        ans = max(ans, cand)
    elif index < n:
        time1, time2 = d[index], 24 - d[index]
        if time1 not in time_set:
            dfs(time_set | {time1}, index+1)
        if time2 not in time_set:
            dfs(time_set | {time2}, index+1)
dfs(set(),0)
print(ans)