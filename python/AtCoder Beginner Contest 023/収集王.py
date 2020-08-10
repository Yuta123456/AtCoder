r,c,k = map(int, input().split())
n = int(input())
row = dict()
row_count = [0 for i in range(r+1)]
column_count = [0 for i in range(c+1)]
column = dict()
candy_locate = set()
for i in range(n):
    r_1,c_1 = map(int, input().split())
    candy_locate.add((r_1,c_1))
    row_count[r_1] += 1
    column_count[c_1] += 1
for i in range(1, r+1):
    if row_count[i] in row:
        row[row_count[i]] += 1
    else:
        row[row_count[i]] = 1
for i in range(1, c+1):
    if column_count[i] in column:
        column[column_count[i]] += 1
    else:
        column[column_count[i]] = 1
ans = 0
#まず、適当にやって大雑把な答え求める
for i in range(k+1):
    if i in row and k-i in column:
        ans += row[i] * column[k-i]
#そのあとで、詰めていく。飴ちゃんがある行と列について調べる。
for x,y in candy_locate:
    if row_count[x] + column_count[y] == k:
        ans -= 1
    elif row_count[x] + column_count[y] == k+1:
        ans += 1
print(ans)
