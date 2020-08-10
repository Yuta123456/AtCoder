a = gets.chomp.to_i
b = gets.chomp.to_i
if b > a 
    puts [(b - a), (a + 10 - b)].min
else
    puts [(a - b), (b + 10 - a)].min
end