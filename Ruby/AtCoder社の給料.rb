n = gets.chomp.to_i
sum = 0
for i in 0...n
    sum += 10000 * (i+1)
end
puts sum / n