n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
point_start_with = [0 for i in range(n)]
roop_count = [1 for i in range(n)]
for i in range(n):
    now = (i + 1)
    now_score = 0
    while p[now - 1] != (i + 1):
        now = p[now - 1]
        now_score += c[now - 1]
        roop_count[i] += 1
    point_start_with[i] = now_score
# 多分0でいい
ans = -(10**9 * 5000)
for i in range(n):
    # iからスタートする場合
    score = 0
    remain_move = 0
    cand_score = 0
    if point_start_with[i] + c[i] > 0 and k > roop_count[i]:
        # 一周以上する可能性がある場合
        # n週して、残りの動ける回数
        # print("Yes")
        round_count = (k // roop_count[i]) - 1
        remain_move = k - round_count * roop_count[i]
        cand_score = round_count * ( point_start_with[i] + c[i] )
    else:
        remain_move = min(k,roop_count[i])
        score = -(10**9 * 5000)
        cand_score = 0
    now = i
    for j in range(remain_move):
        now = p[now] - 1
        cand_score += c[now]
        score = max(score, cand_score)
    # print("start : {}  score : {}".format(i,score))
    ans = max(score, ans)
print(ans)
