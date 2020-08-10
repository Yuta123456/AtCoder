n = int(input())
ac = 0
tle = 0
wa = 0
re = 0
for i in range(n):
    s = input()
    if s == 'WA':
        wa += 1
    elif s == 'RE':
        re += 1
    elif s == "TLE":
        tle += 1
    else:
        ac += 1
print("AC x {}".format(ac))
print("WA x {}".format(wa))
print("TLE x {}".format(tle))
print("RE x {}".format(re))