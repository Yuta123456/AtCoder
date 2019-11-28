n = gets.chomp.to_i
s = {}
t = {}
for i in 0...n
    k = gets.chomp
    if s.key?(k)
        s[k] += 1
    else
        s[k] = 1
        t[k] = 0
    end
end
m = gets.chomp.to_i
for i in 0...m
    k = gets.chomp
    if t.key?(k)
        t[k] += 1
    else
        t[k] = 1
    end
end
max_ans = 0
for i in s.keys
    if s[i] - t[i] > max_ans
        max_ans = s[i] - t[i]
    end
end
print(max_ans)