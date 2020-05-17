import sys
sys.setrecursionlimit(10**7)
s = input()
ans = set()
def dfs(start, count, string):
    global ans 
    if count == 3 or start + count >= len(s):
        ans.add(string)
    else:
        dfs(start,count+1,string + s[start + count])
        dfs(start,count+1,string + '.')
        ans.add(string)
for i in range(len(s)):
    ans.add(s[i])
    dfs(i,0,"")
print(len(ans)-1)
