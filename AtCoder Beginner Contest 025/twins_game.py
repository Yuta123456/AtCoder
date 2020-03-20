import copy
b = []
c = []
total = 0
for i in range(2):
    b.append(list(map(int, input().split())))
    total += sum(b[i])
for i in range(3):
    c.append(list(map(int, input().split())))
    total += sum(c[i])
#print(total)
def score_Check(board):
    naoko = 0
    chokudai = 0
    for i in range(3):
        for j in range(2):
            if board[i][j] == board[i][j+1]:
                chokudai += c[i][j]
            else:
                naoko += c[i][j]
            if board[j][i] == board[j+1][i]:
                chokudai += b[j][i]
            else:
                naoko += b[j][i]
    return chokudai
def cal(count):
    if count < 9:
        if count % 2 == 0:
            ans = -total
            for i in range(3):
                for j in range(3):
                    if graph[i][j] == '*':                        
                        graph[i][j] = '○'
                        ans = max(ans, cal(count + 1))
                        graph[i][j] = '*'
            return ans
        else:
            ans = total
            for i in range(3):
                for j in range(3):
                    if graph[i][j] == '*':
                        graph[i][j] = '×'
                        ans = min(ans, cal(count + 1))
                        graph[i][j] = '*'
            return ans
    else:
        return score_Check(graph)
graph = [['*' for i in range(3)] for j in range(3)]
k = cal(0)
print(k)
print(total - k)
