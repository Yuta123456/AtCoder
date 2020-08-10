#うまくグルーピングしてあげればおｋ
#奇数の場合,一番大きい数字をソロ、それ以外は2個ずついい感じで分ける
#偶数の場合は、i番目に大きいやつとi番目に小さいやつをペア
n = int(input())
ans = []
if n % 2 == 0:
    for i in range(1,n+1):
        for j in range(i,n+1):
            #自分と、自分のペア以外に辺を張る
            if j != i and i + j != n + 1:
                ans.append([i,j])
    print(len(ans))
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]))
else:
    for i in range(1,n):
        #頂点nからは全ての辺に対して張る
        ans.append([n,i])
        for j in range(i,n):
            #自分と、自分のペア以外に辺を張る
            if j != i and i + j != n:
                ans.append([i,j])
    print(len(ans))
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]))