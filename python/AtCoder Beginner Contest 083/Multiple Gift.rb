x,y = gets.chomp.split(" ").map(&:to_i)
k = x
ans = 1
while k * 2 <= y
    k *= 2
    ans += 1
end
print(ans)  