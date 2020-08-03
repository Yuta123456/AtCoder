d = int(input())
c = list(map(int, input().split()))
score = []
for i in range(d):
    score.append(list(map(int, input().split())))
last_day = [0 for i in range(26)]
k = 0
for i in range(d):
    ans = 0
    max_score = -10**9
    for j in range(1, 27):
        s = score[i][j-1]
        for k in range(1,27):
            if j == k:
                continue
            else:
                s -= c[k-1] * (i+1 - last_day[k-1])
        if s > max_score:
            ans = j
            max_score = s
    last_day[ans-1] = i+1
    print(ans)