require 'set'
n = gets.chomp.to_i
a = Set.new
for i in 0...n
    a.add(gets.chomp.to_i)
end
array = a.to_a
array = array.sort()
puts array[-2]