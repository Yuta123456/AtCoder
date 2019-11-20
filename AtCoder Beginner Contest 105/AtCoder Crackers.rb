n, k = gets.chomp.split.map(&:to_i)
if n % k == 0
    print(0)
else
    print(1)
end