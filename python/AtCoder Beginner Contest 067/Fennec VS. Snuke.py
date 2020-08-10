from collections import deque

n = int(input())
node_data = [[] for i in range(n+1)]
node_stuck = deque([])
Fennec = [0] * (n+1)
Snuke = [0] * (n+1)
for i in range(n-1):
    x, y = list(map(int, input().split()))
    node_data[x].append(y)
    node_data[y].append(x)
node_stuck.append([1,0])
finished = set()

while  len(node_stuck) > 0:
    data = node_stuck.pop()
    index = data[0]
    count = data[1]
    finished.add(index)
    Fennec[index] = count
    for i in node_data[index]:
        if i not in finished:
            node_stuck.append([i,count+1])
node_stuck.append([n,0])
finished = set()
while  len(node_stuck) > 0:
    data = node_stuck.pop()
    index = data[0]
    count = data[1]
    finished.add(index)
    Snuke[index] = count
    for i in node_data[index]:
        if i not in finished:
            node_stuck.append([i,count + 1])    
f = 0
s = 0
print("Fennec => {}".format(Fennec))
print("Snuke  => {}".format(Snuke))
for i in range(2, n):
    if Fennec[i] <= Snuke[i]:
        f += 1
    else:
        s += 1

if f > s:
    print("Fennec")
else:
    print("Snuke")
    




