from operator import itemgetter
N = int(input())
X = list(map(int, input().split()))
data = []
for i in range(N):
    data.append([X[i],i])

data.sort()
k = (N//2) - 1
f = data[k][0]
s = data[k+1][0]
#print("f {}  s{}".format(f,s))
data = sorted(data, key = lambda x:x[1])
for i in range(N):
    if data[i][0] <= f:
        print(s)
    else:
        print(f)
