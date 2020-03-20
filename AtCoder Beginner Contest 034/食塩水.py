n, k = map(int, input().split())
salt_water = []
for i in range(n):
    salt_water.append(list(map(int, input().split())))
#salt_water.sort(key=lambda x: x[1], reverse=True)
left = 0.0
right = 100.0
count = 0
def check(target):
    #target以上の濃度の食塩水を作れるかどうかを判定
    salt_water.sort(reverse=True, key=lambda x: x[0]*(x[1] - target))
    salt = 0
    overall = 0
    for i in range(k):
        salt += salt_water[i][0] * salt_water[i][1] / 100
        overall += salt_water[i][0]
    if (salt / overall)*100 >= target:
        return True
    else:
        return False
while count < 300:
    #print("left:{} right:{}".format(left, right))
    mid = (right + left) / 2
    if check(mid):
        left = mid
    else:
        right = mid
    count += 1
print((right + left)/2)