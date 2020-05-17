def check(s,t):
    if (0 <=  s <= h - 1) and (0 <= t <= w - 1):
        return True
    else:
        return False
def grid_2_graph(grid):
    adjacent_list = [[] for i in range(h*w+1)]
    for i in range(h):
        for j in range(w):
            for n_x,n_y in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if check(n_x,n_y):
                    #(i,j) -> (n_y, n_x)に辺をつなぐ
                    adjacent_list[i*w+j].append([(n_y)*w + (n_y),grid[n_y][n_x]])
    return adjacent_list

