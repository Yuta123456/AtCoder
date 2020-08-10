n = int(input())
memo = [{} for i in range(n+1)]
mod = 10**9+7
#想定解法の写経
def ok(last4):
    #隣接する二つを入れ替えてAGC二ならないかどうかをチェック
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i], t[i-1] = t[i-1], t[i]
        if "".join(t).count('AGC') >= 1:
            return False
    return True
def dfs(now, last3):
    if last3 in memo[now]:
        return memo[now][last3]
    if now == n:
        return 1
    ret = 0
    for i in 'AGCT':
        #もし、次の一文字を足した4文字がずらしてAGCに引っかからなければ
        if ok(last3 + i):
            #今回をiにした場合のこの後の文字列の数を全て計算
            ret = (ret + dfs(now+1, last3[1:] + i)) % mod
    memo[now][last3] = ret
    return ret
print(dfs(0,'TTT'))
