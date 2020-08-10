require 'set'
w = gets.chomp
ans = ''
mother = Set['a', 'i', 'u', 'e', 'o']
for i in 0...w.length
    if ! mother.include?(w[i])
        ans += w[i]
    end
end
puts ans
    
