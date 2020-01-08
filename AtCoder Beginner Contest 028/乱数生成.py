s = input()
ans = dict()
ans["A"] = 0
ans["B"] = 0
ans["C"] = 0
ans["D"] = 0
ans["E"] = 0
ans["F"] = 0
for i in range(len(s)):
    if s[i] in ans:
        ans[s[i]] += 1
print("{} {} {} {} {} {}".format(ans["A"],ans["B"],ans["C"],ans["D"],ans["E"],ans["F"]))