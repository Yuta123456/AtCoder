from bisect import bisect_right
# 解法
# 1. xを昇順にソートする。
# 2. xを小さいほうから見ていき、今見ている町よりx, y共に小さい町とマージする
# 3. マージした後、今の街のy座標を
n = int(input())
data = []
for i in range(n):
    data.append([i] + list(map(int, input().split())))
data.sort(key=lambda x:x[1])
print(data)

