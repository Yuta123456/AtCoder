n = int(input())
data = [[]for i in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        data[i].append(list(map(int, input().split())))
max_honest = 0
def bfs(honest):
    if len(honest) == n:
        global max_honest
        for i in range(len(data)):
            if honest[i] == 1:
                for j in data[i]:
                    target, istrue = j
                    if (honest[target-1] == 1 and istrue == 0) or (honest[target-1] == 0 and istrue == 1):
                        return
            else:
                continue
        max_honest = max(max_honest, honest.count(1))
    else:
        bfs(honest + [0])
        bfs(honest + [1])
bfs([])
print(max_honest)


