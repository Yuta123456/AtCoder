n, a, b = gets.chomp.split.map(&:to_i)
if n * a < b
    print(n*a)
else
    print(b)
end