#input
n = int(input())
a = list(map(int, input().split()))

ans = 0
#辞書型でデータを管理
dict = {}
for i in range(n):
    if a[i] not in dict:
        dict[a[i]] = 1
    else:
        dict[a[i]] += 1
for i in dict.keys():
    if i < dict[i]:
        #多い場合は減らすのが確定
        ans += dict[i] - i
    elif i > dict[i]:
        ans += dict[i]
print(ans)
