a = gets.split(' ').map(&:to_i)
a.sort!
print(a[1] + a[0] + a[2] * 10)