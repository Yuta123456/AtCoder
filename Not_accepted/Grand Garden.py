def calc(l,r,count,flower):
    if len(flower) == 0:
        return
    if min(flower) == 0 and max(flower) == 0:
        return
    elif len(flower) == 1:
        count += flower[0]
        flower[0] = 0
        return
    elif min(flower) > 0:
        flower = list(map(lambda x: x - min(flower), flower[l:r]))
        count += min(flower)
        calc(l,r,count,flower)
    else:
        for i in range(len(flower)):
            if flower[i] == 0:
                r = i - 1
                calc(l,r,count,flower)
                l = i + 1

count = 0
n = int(input())
flower = list(map(int, input().split()))
calc(0, n - 1,count,flower)
print(count)
