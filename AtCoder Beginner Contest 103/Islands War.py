n ,m = list(map(int, input().split()))
q = []
for i in range(m):
    q.append(list(map(int, input().split())))
def cal(data):
    return data[1] - data[0]
    
a =  sorted(q, key=cal)
