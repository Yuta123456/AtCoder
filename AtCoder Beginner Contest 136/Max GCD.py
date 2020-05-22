n, k = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)
ans = 0
def try_ans(target):
    remain = [i % target for i in a]
    remain.sort()
    count = 10**10
    #sum_remainは全てをマイナス側に落とし込むときの操作回数
    sum_remain = sum(remain)
    #plus_remainはプラス側に落とし込むときの操作回数
    plus_remain = 0
    for i in range(n-1,-1,-1):
        plus_remain += target - remain[i]
        sum_remain -= remain[i]
        count = min(count, max(sum_remain,plus_remain))
    return count <= k

for i in range(1,int(sum_a**0.5)+1):
    if sum_a % i == 0:
        if try_ans(i):
            ans = max(ans, i)
        if try_ans(sum_a // i):
            ans = max(ans, sum_a//i)
print(ans)
