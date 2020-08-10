n = input()
n = list(map(int, list(n)))
sum_n = sum(n)
digit = (sum_n + 9 - 1) // 9
ans = [1 for i in range(digit)]
sum_n -= digit
for i in range(digit-1,-1,-1):
    if sum_n > 0:
        ans[i] += min(8,sum_n)
        sum_n -= 8
    else:
        break
#もしつくったやつと答えが一緒になっちゃったら
if "".join(map(str,n)) == "".join(map(str,ans)):
    if len(ans) == 1:
        ans = [0] + ans
    if ans[0] == 9:
        sum_n = sum(n)
        digit = (sum_n + 9 - 1) // 9
        digit += 1
        ans = [1 for i in range(digit)]
        sum_n -= digit
        for i in range(digit-1,-1,-1):
            if sum_n > 0:
                ans[i] += min(8,sum_n)
                sum_n -= 8
            else:
                break
        n = ans
    else:
        ans[0] += 1
        ans[1] -= 1
    print("".join(map(str,ans)))
    exit()
for i in range(digit):
    print(ans[i], end="")


