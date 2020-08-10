n = gets.chomp
sum_n = 0
for i in 0...n.length
    sum_n += n[i].to_i
end
if n.to_i % sum_n == 0
    print("Yes")
else
    print("No")
end
