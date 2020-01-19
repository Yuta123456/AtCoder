n = int(input())
global ans
ans = (-1) * 10 ** 15
point = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1,n):
    k = list(map(int, input().split()))
    for j in range(i,n):
        point[i][j+1] = k[j-i]
        point[j+1][i] = k[j-i]
def check(li):
    if len(li) == n:
        global ans
        #group
        total = 0
        one = []
        two = []
        three = []
        for i in range(n):
            if li[i] == 1:
                one.append(i+1)
            elif li[i] == 2:
                two.append(i+1)
            else:
                three.append(i+1)
        if len(one) != 0:
            for i in one:
                for j in one:
                    total += point[i][j]
        if len(two) != 0:
            for i in two:
                for j in two:
                    total += point[i][j]    
        if len(three) != 0:
            for i in three:
                for j in three:
                    total += point[i][j]
        ans = max(ans, total)
    else:
        check(li + [1])
        check(li + [2])
        check(li + [3])    
check([])
print(ans//2)
