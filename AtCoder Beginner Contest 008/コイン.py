import math
n = int(input())
c = []
for i in range(n):
    c.append(int(input()))
c.sort()
ans = 0
memo = dict()
def combi(x, y):
    if x < y:
        return 0
    if (x,y) in memo:
        return memo[(x,y)]
    else:
        memo[(x,y)]  = math.factorial(x) / (math.factorial(x - y) * math.factorial(y))
        return memo[(x,y)]
#preprocess
#自分のことをひっくりかえせるコインの枚数をそれぞれ求める。
#自分は含めないんだけど、実装が簡単だから、すでに自分は引いている状態
turn_over = [-1 for i in range(n)]
for i in range(n):
    for j in range(n):
        if c[i] % c[j] == 0:
            turn_over[i] += 1
#全ての要素に対して
for i in range(n):
    #自分が何番目かを固定
    for no in range(n):
        #自分のことをひっくりかえせる要素の個数
        turn = turn_over[i]
        #自分のことをひっくりかえせないやつ
        #自分は除くから-1
        not_turn = n - turn - 1
        #自分の左にひっくりかえせるやつを何個置くかを固定
        for count in range(0,no+1,2):
            #print("coin = {},  no = {},  count = {},  + :{}".format(c[i],no,count,combi(turn, count) * combi(not_turn, no - count)))
            ans += combi(turn, count) * combi(not_turn, no - count) * math.factorial(no) * math.factorial(n - no - 1)
print(ans / math.factorial(n))
