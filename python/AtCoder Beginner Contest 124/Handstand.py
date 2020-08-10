n, k = list(map(int, input().split()))
s = input()
#尺取り法
right = -1
left = -1
now_k = 0
while right + 1 < n and s[right + 1] == '1': 
    right += 1
#初めのrightの位置を決める
while now_k < k:
    now_k += 1
    while right + 1 < n and s[right + 1] == '0':
        right += 1
    while right + 1 < n and s[right + 1] == '1':
        right += 1
#今の時点で、rightがいい感じの場所にいる。
ans = (right + 1)
while right + 1 < n:
    while right + 1 < n and s[right + 1] == '0':
        right += 1
    while right + 1 < n and s[right + 1] == '1':
        right += 1
    while left + 1 < n and s[left + 1] == '1':
        left += 1
    while left + 1 < n and s[left + 1] == '0':
        left += 1
    left += 1
    ans = max(ans, right - left + 1)
print(ans)

