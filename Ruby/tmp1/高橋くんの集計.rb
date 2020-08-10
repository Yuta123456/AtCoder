n = gets.chomp.to_i
a = gets.chomp.split.map(&:to_i)
ans = 0
count = 0
for i in 0...n
    if a[i] != 0
        count += 1
        ans += a[i]
    end
end
puts (ans  + count -1 ) / count