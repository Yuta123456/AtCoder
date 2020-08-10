n, k = map(int, input().split())
if k > (n - 1) * (n - 2) / 2:
    print(-1)
else:
    #頂点1を中心のスター型グラフを作る
    ans = []
    appended_edges = set()
    for i in range(2,n+1):
        ans.append([1,i])
        appended_edges.add((1,i))
    #そのあとで、いらない分だけ頂点をつなげばいい
    flag = False
    #いま、最短距離が2の頂点の数
    count = (n-1)*(n-2) / 2
    for i in range(2,n+1):
        for j in range(i,n+1):
            if k == count:
                flag = True
                break
            if (i,j) not in appended_edges and i != j:
                ans.append([i,j])
                appended_edges.add((i,j))
                count -= 1
        if flag:
            break
    print(len(ans))
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]))
