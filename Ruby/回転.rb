c = []
for i in 0...4
    c.push(gets.chomp)
end
for i in (0...4).to_a.reverse()
    puts c[i].reverse()
end