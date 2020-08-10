n = int(input())
payroll = [-1 for i in range(n+2)]
junior = [[] for i in range(n+1)]
for i in range(n-1):
    k = int(input())
    junior[k].append(i+2)

def cul(number):
    if len(junior[number]) == 0:
        payroll[number] = 1
        return 1
    elif payroll[number] != -1:
        return payroll[number]
    else:
        pay_li = [cul(i) for i in junior[number]]
        payroll[number] = max(pay_li) + min(pay_li) + 1
        return payroll[number]

print(cul(1))