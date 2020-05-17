import bisect
n, k = map(int, input().split())
a = list(map(int, input().split()))
negative_number_cnt = 0
positive_number_cnt = 0
negative_number = []
positive_number = []
zero_cnt = 0
a.sort()
def binary_search(left, right,positive):
    if right - left <= 1:
        return right
    middle = (right + left) // 2
    if is_can(middle,positive):
        return binary_search(left, middle,positive)
    else:
        return binary_search(middle, right,positive)
def is_can(x,positive):
    #xよりも小さい値がk個あるかどうか？
    if positive:
        count = than_less_zero
        #正＊正
        r = len(positive_number)-1
        for l in range(len(positive_number)):
            while l < r and positive_number[l] * positive_number[r] > x:
                r -= 1
            count += r - l
            if l >= r:
                break
        #負*負
        r = len(negative_number)-1
        for l in range(len(negative_number)):
            while l < r and r_negative_number[l] * r_negative_number[r] > x:
                r -= 1
            count += r - l
            if l >= r:
                break
        #print("target:{} count:{}".format(x,count))
        if count >= k:
            return True
        else:
            return False
    else:
        count = 0
        l,r = 0,0
        for l in range(len(negative_number)):
            while r < len(positive_number) and positive_number[r] * negative_number[l] > x:
                r += 1
            count += len(positive_number) - r
        if count >= k:
            return True
        else:
            return False



for i in range(n):
    if a[i] > 0:
        positive_number_cnt += 1
        positive_number.append(a[i])
    elif a[i] < 0:
        negative_number_cnt += 1
        negative_number.append(a[i])
    else:
        zero_cnt += 1
than_less_zero = ( negative_number_cnt * positive_number_cnt ) + (zero_cnt * (zero_cnt-1)//2) + zero_cnt * (n-zero_cnt)
r_negative_number = [negative_number[i] for i in range(len(negative_number)-1,-1,-1)]

if than_less_zero < k:
    #答えが正になる
    print(binary_search(0,10**20,True))
elif ( negative_number_cnt * positive_number_cnt ) < k:
    #答えが0になる
    print(0)
else:
    #答えが負になる
    print(binary_search(-10**20,5,False))
