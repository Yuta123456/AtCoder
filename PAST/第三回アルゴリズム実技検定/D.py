n = int(input())
grid = []
num_f = [
    ".###..#..###.###.#.#.###.###.###.###.###.",
    ".#.#.##....#...#.#.#.#...#.....#.#.#.#.#.",
    ".#.#..#..###.###.###.###.###...#.###.###.",
    ".#.#..#..#.....#...#...#.#.#...#.#.#...#.",
    ".###.###.###.###...#.###.###...#.###.###.",
]
for i in range(5):
    grid.append(list(input()))
ans = []
num_format = [[] for i in range(10)]
for i in range(10):
    for j in range(5):
        num_format[i].append(num_f[j][4*i:4*i+4])

for i in range(n):
    for num in range(10):
        flag = True
        for row in range(5):
            for column in range(4): 
               if num_format[num][row][column] != grid[row][4*i+column]:
                    flag = False
                    break
        if flag:
            ans.append(num)
            break
print("".join(map(str, ans)))
