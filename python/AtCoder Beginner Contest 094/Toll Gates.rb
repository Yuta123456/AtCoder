n, m, x = gets.chomp.split(" ").map(&:to_i)
a = gets.chomp.split(" ").map(&:to_i)
for i in 0..(a.length - 1)
    if a[i] > x
        k = i
        break
    end
end
print([k,a.length - k].min)