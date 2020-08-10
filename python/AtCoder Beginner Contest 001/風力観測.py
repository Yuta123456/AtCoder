deg, dis = map(int, input().split())
ans_1 = ''
ans_2 = ''
if 0 <= deg < 112.5:
    ans_1 = 'N'
elif deg < 337.5:
    ans_1 = 'NNE'
elif deg < 562.5:
    ans_1 = 'NE'
elif deg < 787.5:
    ans_1 = 'ENE'
elif deg < 1012.5:
    ans_1 = 'E'
elif  deg < 1237.5:
    ans_1 = 'ESE'
elif  deg < 1462.5:
    ans_1 = 'SE'
elif  deg < 1687.5:
    ans_1 = 'SSE'
elif deg < 1912.5:
    ans_1 = 'S'
elif deg < 2137.5:
    ans_1 = 'SSW'
elif deg < 2362.5:
    ans_1 = 'SW'
elif  deg < 2587.5:
    ans_1 = 'WSW'
elif  deg < 2812.5:
    ans_1 = 'W'
elif  deg < 3037.5:
    ans_1 = 'WNW'
elif  deg < 3262.5:
    ans_1 = 'NW'
elif  deg < 3487.5:
    ans_1 = 'NNW'
else:
    ans_1 = 'N'
def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p
#風力計算
dis = my_round(dis / 60, 1)
#今、disは秒速の状態
if dis < 0.3:
    ans_1 = 'C'
    ans_2 = 0
elif dis < 1.6:
    ans_2 = 1
elif dis < 3.4:
    ans_2 = 2
elif dis < 5.5:
    ans_2 = 3
elif dis < 8.0:
    ans_2 = 4
elif dis < 10.8:
    ans_2 = 5
elif dis < 13.9:
    ans_2 = 6
elif dis < 17.2:
    ans_2 = 7
elif dis < 20.8:
    ans_2 = 8
elif dis < 24.5:
    ans_2 = 9
elif dis < 28.5:
    ans_2 = 10
elif dis < 32.7:
    ans_2 = 11
else:
    ans_2 = 12
print("{} {}".format(ans_1, ans_2))   