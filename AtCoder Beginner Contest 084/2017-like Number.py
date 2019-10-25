import math
import bisect
#下準備
num = (10**5) + 2
#エラトステネス
era = [i for i in range(3,num,2)]
i = 0
while era[i] <= math.sqrt(num):
    tmp = era[i]
    era = [j for j in era if j % era[i] != 0]
    era.insert(i,tmp)
    i += 1
#もう一個の奴もやる

era = [j for j in era if bisect.bisect_left(era,(j+1) // 2) != bisect.bisect_right(era,(j+1)//2)]
era.insert(0,3)
#ans[i] => iまでの、目的を満たす数字の個数
q = int(input())
for i in range(q):
    l,r = list(map(int, input().split()))
    print(bisect.bisect_right(era,r) - bisect.bisect_left(era,l))
