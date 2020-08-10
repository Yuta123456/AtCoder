a = gets.chomp.split.map(&:to_i)
a.sort!
print(a[0] + a[1])