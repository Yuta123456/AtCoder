n,m,q = map(int, input().split())
now_solve = [[] for i in range(n+1)]
problem_point = [n for i in range(m+1)]
for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        ans = 0
        #print("{}: {}".format(s[1], now_solve[s[1]]))
        for i in now_solve[s[1]]:
            ans += problem_point[i]
        print(ans)
    else:
        problem = s[2]
        problem_point[problem] -= 1
        now_solve[s[1]].append(problem)
