n = int(input())
s = list(input())
global data
data = [[0 for i in range(n)] for j in range(2)]

for i in range(n):
    data[0][i] = s[i]
    #data[i][1]はペアがいるかどうかの判定
    data[1][i] = 0
#左向きに探していく
#ペアが見つからなければ挿入する。
def Lsearch(index):
    while index >= 0:
        if data[0][index] == '(' and data[1][index] == 0:
            data[1][index] = 1
            return False
        index -= 1
    return True
#右向きに探しに行く
def Rsearch(index):
    if index >= len(data[0]):
        data[0].insert(len(data[0]), ')')
        data[1].insert(len(data[0]), 1)
        return
    elif data[0][index] == ')' and data[1][index] == 0:
        data[1][index] = 1
    else:
        Rsearch(index + 1)
i = 0
while i < len(data[0]):
    #print(data[1])
    #相手が見つかっていれば終わり
    # ) で、相手が見つかっていなければ左側を探す
    if data[0][i] == ')' and data[1][i] == 0:
        if Lsearch(i - 1):
            data[1][i] = 1
            data[0].insert(0, '(')
            data[1].insert(0, 1)
    # ( で、相手が見つかっていなければ、右側を探す
    elif data[0][i] == '(' and data[1][i] == 0:
        Rsearch(i + 1)
        data[1][i] = 1
    i += 1
print("".join(data[0]))
#再帰の書き方はたぶんあってるはずだが、なぜかindexが184やら311やらに初期化されてしまう