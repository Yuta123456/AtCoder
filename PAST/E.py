import copy
n , q = map(int, input().split())
s = []
for i in range(q):
    s.append(input())
graph = [["N" for i in range(n+1)] for j in range(n+1)]
for i in range(q):
    input_s = s[i].split()
    if input_s[0] == '1':
        a,b = int(input_s[1]), int(input_s[2])
        graph[a][b] = "Y"
    elif input_s[0] == "2":
        a = int(input_s[1])
        for j in range(1,n+1):
            if graph[j][a] == "Y":
                graph[a][j] = "Y"
    else:
        a = int(input_s[1])
        rr = copy.deepcopy(graph[a])
        for j in range(1,n+1):
            if rr[j] == "Y":
                for k in range(1,n+1):
                    if graph[j][k] == "Y":
                        graph[a][k] = "Y"
for i in range(n+1):
    graph[i][i] = "N"
for i in range(1,n+1):
    print("".join(graph[i][1:]))
