n = gets.chomp.to_i
d, x = gets.chomp.split(" ").map(&:to_i)
a = []
for i in 0...n
    a[i] = gets.chomp.to_i
end
x += n
for i in 0...n
    x += d / a[i]
    if d % a[i] == 0
        x -= 1
    end
end
print(x)