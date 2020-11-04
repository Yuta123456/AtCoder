inp = list(map(int, input().split()))
while inp:
    n, m, t, p = inp
    fold = []

    for i in range(t):
        fold.append(list(map(int, input().split())))
    hole = []

    for i in range(p):
        hole.append(list(map(int, input().split())))
    paper = [[1 for i in range(n)] for j in range(m)]

    for i in range(t):
        d, c = fold[i]
        new_paper = []
        if d == 1:
            if c > (len(paper[0]) // 2):
                
            for j in range(c):
                for k in range(len(paper)):
                    paper[k][2*c - j - 1] += paper[k][j]
                    paper[k][j] = 0
            new_paper = [paper[q][c:] for q in range(len(paper))]
        else:
            for j in range(len(paper) - c, len(paper)):
                for k in range(len(paper[0])):
                    paper[2 * len(paper) - 2 * c - j - 1][k] += paper[j][k]
                    paper[j][k] = 0
            new_paper = paper[:-c]
        paper = new_paper
    print("fold finish")
    for q in range(p):
        x, y = hole[q]
        print(paper[-y][x])
    inp = list(map(int, input().split()))
    if inp == [0,0,0,0]:
        exit()