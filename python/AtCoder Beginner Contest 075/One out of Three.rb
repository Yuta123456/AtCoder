a,b,c = gets.chomp.split.map(&:to_i)
if a == b
    print(c)
elsif a == c
    print(b)
else
    print(a)
end