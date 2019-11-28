n, x = gets.chomp.split(" ").map(&:to_i)
m = []
for i in 0..(n - 1)
    m[i] = gets.chomp.to_i
end
ans = n + (x - m.inject(:+)) / (m.min)
print(ans)
