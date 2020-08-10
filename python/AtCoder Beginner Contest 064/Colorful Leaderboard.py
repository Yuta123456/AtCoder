import bisect
n = int(input())
a = list(map(int, input().split()))
a.sort()
color = 0
pre_rate = 0
#3200以上の人のカウント
free = 0

for i in range(1,9):
    #400刻みで考えていき、さっきの同じところに挿入されるかどうか確認
    if bisect.bisect_left(a, 400 * i) != pre_rate:
        #挿入されないということは、間に人がいるということなので、一色足す。
        color += 1
        #前のレートの添え字の更新
        pre_rate = bisect.bisect_left(a, 400 * i)
#3200以上の人は何人いるか数える
free = n - bisect.bisect_left(a,3200)
#出力。最小値は1を下回らず、最大値は⒏を超えないようにする。
#freeの人は色が被らないのが最大なため、足せるだけ足した後に⒏と比較
print("{} {}".format(max(1, color), min(8,free + color)))