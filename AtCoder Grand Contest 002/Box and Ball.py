n, m = map(int, input().split())
#全部シュミレートして、0個だったやつは弾く
#赤いボールが入っている可能性があったもの、からうつったものもすべて候補に入る
candidate = set([1])
ball = [1 for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    if x in candidate:
        candidate.add(y)
    else:
        if ball[y] == 0 and y in candidate:
            candidate.remove(y)
    ball[x] -= 1
    ball[y] += 1
for i in range(1,n+1):
    if ball[i] == 0 and i in candidate:
        candidate.remove(i)
print(len(candidate))    