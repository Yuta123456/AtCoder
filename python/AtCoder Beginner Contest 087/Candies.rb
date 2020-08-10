$n = gets.chomp.to_i
$a = []
$a[0] = gets.chomp.split(" ").map(&:to_i)
$a[1] = gets.chomp.split(" ").map(&:to_i)
$max = 0
def dfs(x,y,count)
    if y == 1 and x == $n-1
        $max = [count + $a[y][x], $max].max
    else
        if y >= 1
            dfs(x+1,y,count + $a[y][x])
        elsif x >= ($n - 1)
          dfs(x, y+1,count + $a[y][x])
        else
            dfs(x+1,y,count + $a[y][x])
            dfs(x,y+1,count + $a[y][x])
        end
    end
end
dfs(0,0,0)
print($max)