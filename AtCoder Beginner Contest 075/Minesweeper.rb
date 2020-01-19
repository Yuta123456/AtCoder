h, w = gets.chomp.split.map(&:to_i)
s = []
for i in 0...h
    s.push(gets.chomp.split(//))
end
for i in 0...h
    for j in 0...w
        if s[i][j] == '#'
            for k in -1..1
                for l in -1..1
                    if  i + k < 0 or i + k >= h or j + l < 0 or j + l >= w
                        next
                    end
                    if s[i+k][j+l] == '.'
                        s[i+k][j+l] = 1
                    elsif s[i+k][j+l] == '#'
                        next
                    else
                        s[i+k][j+l] += 1
                    end
                end
            end
        end
    end
end
for i in 0...h
    for j in 0...w
        if s[i][j] == '.'
            s[i][j] = 0
        end
    end
end
for i in 0...h
    print(s[i].join())
    puts
end