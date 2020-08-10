
n = int(input())
now = [1,1]
data = []

for i in range(n):
    data.append(list(map(int, input().split())))
for i in range(n):
    t,a = data[i]
    mul = max((now[0] + t - 1)//t, (now[1] + a - 1) //a)
    now = list(map(lambda x:x*mul, data[i]))
print(sum(now))