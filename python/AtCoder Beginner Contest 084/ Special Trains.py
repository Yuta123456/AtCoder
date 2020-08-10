#input

n = int(input())
c = [0 for i in range(n-1)]
s = [0 for i in range(n-1)]
f = [0 for i in range(n-1)]
for i in range(n-1):
    c[i], s[i], f[i] = list(map(int, input().split()))

#引数　（始まりの駅, 現在の時間）
def calcTime(start, time):

    #着いていたら、現在の時間を返す
    if start == n - 1:
        return time
    #発車時刻より早くついてしまった場合は、発車時刻まで待つ
    if time < s[start]:
        time = s[start]
    #発車時刻より後でも、f[i]の倍数でないと電車が発車しないため、そこまで待つ
    if time % f[start] != 0:
        time += f[start] - (time % f[start])
    #次の駅に着いた時間
    time += c[start]
    #次の駅に着いたので、次の駅の時間を求める。
    return calcTime(start + 1, time)
for i in range(n):
    print(calcTime(i, 0))
