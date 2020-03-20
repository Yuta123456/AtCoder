import bisect
n, d, a = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort()
monster_hp = []
monster_x = []
for i in range(n):
    monster_hp.append(data[i][1])
    monster_x.append(data[i][0])
ans = 0
damage_range = [0 for i in range(n+1)]
for i in range(n):
    #step1 i体目のモンスターに入ってるダメージを計算。
    damage_range[i+1] += damage_range[i]
    damage = damage_range[i+1] * a
    if damage < monster_hp[i]:
        #もしこのモンスターが既に致死量でないなら,魔法を打つ必要がある
        min_requaired = (monster_hp[i] - damage + a - 1) // a
        index = bisect.bisect_right(monster_x, monster_x[i] + 2 * d)
        damage_range[i+1] += min_requaired
        if index < n:
            damage_range[min(index+1, n)] -= min_requaired
        ans += min_requaired
print(ans)
    