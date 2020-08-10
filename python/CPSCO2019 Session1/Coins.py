n,k = map(int, input().split())
a = list(map(int, input().split()))
ans = 10**9
def full_search(li,count):
    if count == k:
        calc(li)
    elif len(li) == n:
        return
    else:
        full_search(li + [0], count)
        full_search(li + [1], count+1)
def calc(for_calc):
    payment = 0
    for i in range(len(for_calc)):
        if for_calc[i]:
            payment += a[i]
    #paymentが全ての合計の払う金額
    global ans
    candidate = 0
    s = str(payment)
    for i in s:
        digit = int(i)
        if digit >= 5:
            candidate += (digit - 4)
        else:
            candidate += digit
    ans = min(ans, candidate)
full_search([],0)
print(ans)


