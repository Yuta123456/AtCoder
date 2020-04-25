s = set(list(input()))
ans = "Yes"
if ("N" in s) != ("S" in s):
    ans = "No"
if ("E" in s) != ("W" in s):
    ans = "No"
print(ans)