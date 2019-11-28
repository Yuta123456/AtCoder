a = gets.chomp.to_i
b = gets.chomp.to_i
c = gets.chomp.to_i
d = gets.chomp.to_i
ans = 0
if a >= b
    ans += b
else
    ans += a
end
if c >= d
    ans += d
else
    ans += c
end
print(ans)