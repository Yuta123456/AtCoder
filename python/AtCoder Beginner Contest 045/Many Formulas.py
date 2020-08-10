s = input()
ans = 0
k = len(s)
def search(formulas, n,count):
    global k
    if count >= k:
        cal(formulas)
    else:
        search(formulas,n+1,count + 1)
        search(formulas[:n] + "+" + formulas[n:],n+2,count + 1)
def cal(formulas):
    global ans
    ans += sum(map(int, list(formulas.split("+"))))
search(s,1,1)
print(ans)