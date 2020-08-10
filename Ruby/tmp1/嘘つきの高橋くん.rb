require 'set'

n = gets.chomp.to_i
a, b = gets.chomp.split.map(&:to_i)
k = gets.chomp.to_i
p = gets.chomp.split.map(&:to_i)
set1 = Set.new(p)
if set1.length < k
    puts "NO"
else
    if set1.include?(a) || set1.include?(b) 
        puts "NO"
    else
        puts "YES"
    end
end
