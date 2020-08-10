import bisect
n = int(input())
plan = []
for i in range(n):
    plan.append(list(map(int, input().split())))
plan.sort()
plan_time = [plan[i][0] for i in range(len(plan))]
m = int(input())
for i in range(m):
    t = int(input())
    index = bisect.bisect_left(plan_time, t)
    if index >= n:
         ans = plan[index-1][1] + t - plan[index-1][0]
    else:
        ans = min(plan[index-1][1] + max(0,t - plan[index-1][0]), plan[index][1])
    print(ans)
