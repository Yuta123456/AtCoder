n = int(input())
global count
count = 0
def dfs(s):
    if int(s) > n:
        return 0
    if set(list(s[1:])) == {'3','5','7'}:
        global count
        count += 1
    for i in '753':
        dfs(s + i)
dfs('0')
print(count)
