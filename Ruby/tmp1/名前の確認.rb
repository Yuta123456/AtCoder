s = gets.chomp
s[0] = s[0].upcase
for i in 1...s.length
    s[i] = s[i].downcase
end
puts s