a, b = gets.chomp.split.map(&:to_i)
data = []
data[0] = 0
for i in 1..999
    data[i] = data[i - 1] + i
end
k = b - a
print(data[k] - b)