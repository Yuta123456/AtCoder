n, s, t = gets.chomp.split.map(&:to_i)
ans = 0
w = 0
for i in 0...n
    a = gets.chomp.to_i
    w += a
    if s <= w && w <= t
        ans += 1
    end
end
puts ans 
