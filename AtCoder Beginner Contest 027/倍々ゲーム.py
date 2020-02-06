import math
n = int(input())
ans = ['Takahashi', 'Aoki']
#結局、1が勝ちかどうかを確かめればいいはず。
def win_range(x):
    #一番大きい負けの所をもらう
    if x == 1:
        print(ans[1])
        exit()
    k = x//2 # 一番大きい勝ちの数字
    #ギリギリ、k + 1に入れれる数字が、一番小さい勝ちの数字
    p = (k + 2 - 1) // 2
    if p == 1:
        print(ans[0])
        exit()
    else:
        win_range(p-1)
win_range(n)
